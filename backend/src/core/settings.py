import os 
from core.db_info import DB_LIST

DB_NAME = "MYSQL"

DB_INFO = {
        'ip': f"{DB_NAME}_{os.environ['DB_NAME']}",
        'port' : f"{DB_NAME}_{os.environ['DB_NAME']}",
        'user' : f"{DB_NAME}_{os.environ['DB_NAME']}",
        'pw': f"{DB_NAME}_{os.environ['DB_NAME']}",
        'name': f"{DB_NAME}_{os.environ['DB_NAME']}",
    },


CORS_ORIGINS = [
    "*",
    # "http://localhost",
    # "http://localhost:8080",
]



