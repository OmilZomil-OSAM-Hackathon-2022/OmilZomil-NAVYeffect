
AI_TABLE = {
    'uniform' : {
        1:"정복",
        2:"샘당",
        3:"군복",
    },
}
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
}
FRONT_TABLE = {
    "uniform" : {
        "샘당" : "blue",
        "정복" : "black",
        "군복" : "green",
    }
}
AFFILIATION_TABLE = {
    "샘당" : "해군",
    "정복" : "해군",
    "군복" : "육군",
}
UNIFORM_PARTS = {
    2 : [ "name_tag", "rank_tag ], # 샘당
    3 : [ "name_tag", "rank_tag, "muffler", "neck" ], # 정복
    4 : [ "name_tag", "rank_tag, "flag" ], # 군복
}
