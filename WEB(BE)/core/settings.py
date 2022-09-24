import os 
from core.db_info import DB_LIST

DB_NAME = os.environ['DB_NAME']

DB_INFO = DB_LIST[DB_NAME]