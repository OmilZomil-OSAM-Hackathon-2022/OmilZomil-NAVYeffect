DB_TABLE = {
    "uniform" : {
        "샘당" : 2,
        "정복" : 3,
        "군복" : 4,
    }, 
    "affiliation": {
        "육군": 2, 
        "해군": 3, 
        "공군": 4,
        "해병대": 5, 
    }, 
    "rank" : {
        "이병": 2,
        "일병": 3,
        "상병": 4,
        "병장": 5,
    },
 "두발" : 1,    # "두발"
"name_tag" : 2,   # "이름표" :
"rank_tag" : 3,   # "계급장" : 3,
"태극기" : 4,   #"태극기" : 4,
"모자" : 5,     #"모자" : 5,
"neckerchief" : 6, # "네커치프" : 6,
"머플러" : 7,   #"머플러" : 7,


}

UNIFORM = {
    1 : "black",
    2 : "blue",
    3 : "green",
}

def ai_2_worker(report:dict):
    # 이름 변경 및 숫자를 문자로 변경
    report['uniform'] = UNIFORM[report.pop('dress_kind')]

    return report
    