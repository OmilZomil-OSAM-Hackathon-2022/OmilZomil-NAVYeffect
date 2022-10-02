import os 


DB_INFO = {
        'ip': os.environ['MYSQL_HOST'],
        'port' : 3306,
        'user' : os.environ['MYSQL_USER'],
        'pw': os.environ['MYSQL_PASSWORD'],
        'name': os.environ['MYSQL_DB'],
    }


CORS_ORIGINS = [
    "*",
    # "http://localhost",
    # "http://localhost:8080",
]



