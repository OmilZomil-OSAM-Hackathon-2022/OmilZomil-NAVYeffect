UNIFORM = {
    "blue" : 2,
    "black" : 3,
    "green" : 4,
}
AFFILIATION = {
    "" : 1,
    "army": 2, 
    "navy": 3, 
    "air": 4,
    "marin": 5, 
}
RANK = {
    "" : 1,
    "이병": 2,
    "일병": 3,
    "상병": 4,
    "병장": 5,
}

PART_ID = {
    "hair": 1, 
    "name_tag": 2, 
    "rank_tag: 3, 
    "flag": 4, 
    "cap": 5, 
    "muffler": 6, 
    "neckerchief": 7, 
}

"""

"두발" : 1,    # "두발"
"name_tag" : 2,   # "이름표" :
"rank_tag : 3,   # "계급장" : 3,
"flag" : 4,   #"태극기" : 4,
"모자" : 5,     #"모자" : 5,
"neckerchief" : 6, # "네커치프" : 6,
"머플러" : 7,   #"머플러" : 7,

"""

def ai_2_db_main(report):
    temp = report.copy()
    if temp['uniform'] in UNIFORM.keys():
        temp['uniform'] = UNIFORM[temp['uniform']]
    if temp['affiliation'] in AFFILIATION.keys():
        temp['affiliation'] = AFFILIATION[temp['affiliation']]
    if temp['rank'] in RANK.keys():
        temp['rank'] = RANK[temp['rank']]
    return temp

def get_part_id(part_name):
    return PART_ID[part_name]