UNIFORM = {
    "blue" : 2,
    "black" : 3,
    "green" : 4,
}
AFFILIATION = {
    "army": 2, 
    "navy": 3, 
    "air": 4,
    "marin": 5, 
}
RANK = {
    "이병": 2,
    "일병": 3,
    "상병": 4,
    "병장": 5,
}

"""

"두발" : 1,    # "두발"
"name_tag" : 2,   # "이름표" :
"rank_tag" : 3,   # "계급장" : 3,
"flag" : 4,   #"태극기" : 4,
"모자" : 5,     #"모자" : 5,
"neckerchief" : 6, # "네커치프" : 6,
"머플러" : 7,   #"머플러" : 7,

"""

def ai_2_db_main(report):
    report['uniform'] = UNIFORM[report['uniform']]
    report['affiliation'] = AFFILIATION[report['affiliation']]
    report['rank'] = RANK[report['rank']]
    return report
    