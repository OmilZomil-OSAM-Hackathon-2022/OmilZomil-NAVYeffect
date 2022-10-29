from multiprocessing import Process, Queue

from fastapi import APIRouter, Depends, Body, Request, BackgroundTasks


from app.api.websocket.image import photo_2_img, img_2_photo
from app.ai.OZEngine.model import OmilZomil
from app.api.multi.queue import single_queue

router = APIRouter()

omil_detecter = OmilZomil()

def task1(img):
    result = omil_detecter.detect(img)
    print(result)

    single_queue.put(result)


    print(result)

@router.post("/single")
async def get_body(request: Request, background_tasks: BackgroundTasks):
    json_data = await request.json()
    img = photo_2_img(json_data['photo'])
    background_tasks.add_task(task1, img=img)    
    print("end")
    return {"asd": "asdasd"}