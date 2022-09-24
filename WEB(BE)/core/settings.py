import os 

DB_NAME = os.environ['DB_NAME']

db_list = {
    'docker' : {
        'ip': 'db',
        'port' : 5432,
        'user' : 'user',
        'pw': '1234',
        'name': 'dress',
    }
}

DB_INFO = db_list[DB_NAME]