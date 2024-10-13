from util.sqlite_tools import sqlite_tools

import garth
from garth.exc import GarthException

PATH = "src/database/garmin_data"
TABLE_NAME = "health_stats_by_date"
TEMPLATE = "src/database/schema.sql"

def connect_or_initialize_sqlite_db(path): 
    db = sqlite_tools(path)
    if not db.table_exists(TABLE_NAME):
        db.load_from_sql_file(TEMPLATE)
    return db

# structure to prepare an insertion
def create_or_load_garth_connection(user=None, pwrd=None, path="~/.garth"):
    if user and pwrd:
        garth.login(user, pwrd)
    else:
        garth.resume(path)
    
    try:
        print(garth.client.username)
    except GarthException as ge:
        #TODO: throw better error and messaging
        print("failed to login. please try again")
        raise ge
    
create_or_load_garth_connection()