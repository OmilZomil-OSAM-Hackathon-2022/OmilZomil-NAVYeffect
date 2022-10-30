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
    "class_tag": 3, 
    "flag": 4, 
    "cap": 5, 
    "muffler": 6, 
    "neckerchief": 7, 
}

"""

"두발" : 1,    # "두발"
"name_tag" : 2,   # "이름표" :
"class_tag" : 3,   # "계급장" : 3,
"flag" : 4,   #"태극기" : 4,
"모자" : 5,     #"모자" : 5,
"neckerchief" : 6, # "네커치프" : 6,
"머플러" : 7,   #"머플러" : 7,

"""

def ai_2_db_main(report):
    if report['uniform'] in UNIFORM.keys():
        report['uniform'] = UNIFORM[report['uniform']]
    if report['affiliation'] in AFFILIATION.keys():
        report['affiliation'] = AFFILIATION[report['affiliation']]
    if report['rank'] in RANK.keys():
        report['rank'] = RANK[report['rank']]
    return report

def get_part_id(part_name):
    return PART_ID[part_name]