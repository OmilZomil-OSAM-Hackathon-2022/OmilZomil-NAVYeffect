from datetime import datetime, timedelta
import cv2
import socket
import json
import select
import errno
import time

from app.ai.OZEngine.person_detectors.PersonDetector import PersonDetector
from app.core.config import settings
from app.api.websocket.image import photo_2_img, img_2_photo


EMPTY_PERSON_SECOND = 10
EXPIRATION_COUNT = 5


IP, PORT = settings.WORKER_SERVER

QUEUE_PATH = f"{settings.IMAGE_PATH}/queue"
INSPECTION_PATH = f"{settings.IMAGE_PATH}/inspection"

class SocketBroker:
    person_detector = PersonDetector()

    def __init__(self, id):
        self.id = id
        self.last_person_time = datetime.now() - timedelta(seconds=EMPTY_PERSON_SECOND) # 처음은 무조건 새로운 사람이니깐

        # 소켓 연결
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
        self.socket.connect((IP, PORT))
        self.socket.setblocking(0)
        print("소켓 연결 완료")

        # 5번 이상 업데이트
        self.is_send_task = True

    def add_task(self, photo, guardhouse, work_time):

        # 사람 유무를 판별
        img = photo_2_img(photo)
        person_result = self.person_detector.detect(img)
        
        # 사람이 아니면 무시
        if not person_result:
            print(f" 사람이 아닙니다. 처리를 마칩니다.")
            return {
                "type" : "status",
                "status" : "no human",
            }
        
        # 사람인 경우 이미지 파일 저장
        img_path = f"{QUEUE_PATH}/{guardhouse}_{work_time.strftime('%H-%m-%s')}.jpg"
        cv2.imwrite(img_path, img)

        # 1. 오랜만에 온 사람인 경우 
        if work_time - self.last_person_time > timedelta(seconds=EMPTY_PERSON_SECOND):
            task_msg = {
                "guardhouse" : guardhouse, 
                "path": img_path,
                }
        # 2. 연속적인 사람인 경우
        else:
            task_msg = {
                "path": img_path,
            }

        # 메세지 전송
        print(f" 사람을 확인하였습니다. worker에게 작업을 넘김니다.")

        task_json_msg = json.dumps(task_msg)
        self.socket.sendall(bytes(task_json_msg, 'ascii'))

        # 프론트에게 1차 응답
        return {
            "result" : "status",
            "status" : "send task",
            "task_msg": task_msg,
        }
        
    def receive(self):
        try:
            print(f"처리 완료된 내용이 있는지 확인합니다.")
            data_json = self.socket.recv(1024).strip()

        except socket.error as e:
            err = e.args[0]
            if err == errno.EAGAIN or err == errno.EWOULDBLOCK:    
                time.sleep(0.5)
                return None
            else:
                # a "real" error occurred
                print(e)
                sys.exit(1)
        
            # got a message, do something :)
        else:
            # 수신된 데이터를 list(dict)로 변환합니다.
            data_str = data_json.decode('ascii')
            data_list = data_str.split('{') # json이 여러개인 경우 처리
            data_list.remove('') # 첫번째 값 제거 - json이 여러개 오는 경우를 처리하기 위함
            query_list = list(map(lambda x : json.loads("{"+ x), data_list))

            print(f"수신된 데이터 : {query_list}")

            result_msg_list = []
            for query in query_list:
                result_msg_list.append(self.report(query))
            return result_msg_list
        
    def report(self, query):
        # ai 처리 결과에 따라 broker가 판단
        if query['ai'] == "stop":
            return query    # "ai" : "stop", "step" : ai_step,
        
        # 데이터가 갱신시 count 감소
        if query['ai'] == "update":
            self.is_send_task -= 1
        

        # 메인 이미지 파일을 읽어와 결과 메세지에 첨부한다.
        img = cv2.imread(query['main_path'])
        query['photo'] = img_2_photo(img)      
        