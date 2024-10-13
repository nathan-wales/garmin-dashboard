import sqlite3

# Note: these have not been implemented with command syntax checking in mind. This can likely be abused
# This is a quick and dirty wrapper, do not use with production data
class sqlite_tools:

    def __init__(self, db_file_name) -> None:
        self.db_connection = _connect_or_create(db_file_name)
        self.db_cursor = self.db_connection.cursor()

    def create_table(self, query):
        self._execute_query(query)
        
    def insert(self, query, data=None, execute_many=False):
        if data is None:
            self._execute_query(query)
        elif execute_many:
            self._execute_many(query, data)
        else:
            self._execute_query(query, data)

        self.db_connection.commit()
    
    def select_one(self, query):
        res = self._execute_query(query)
        return res.fetchone()
    
    def select_many(self, query):  
        res = self._execute_query(query)
        return res.fetchall()
    
    def table_exists(self, table_name):
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?;"
        self.db_cursor.execute(query, (table_name,))
        return self.db_cursor.fetchone() is not None
    
    def load_from_sql_file(self, file_path):
        
        with open(file_path, 'r') as file:
            sql_script = file.read()
        
        try:
            self.db_cursor.executescript(sql_script)
            self.db_connection.commit()
            print("SQL script executed successfully.")
        except sqlite3.Error as e:
            raise Exception("Error in sqlite_tools\n" + str(e))

    def _execute_query(self, query):
        try:
            return self.db_cursor.execute(query)
        except Exception as e:
            raise Exception("Error in sqlite_tools\n" + str(e))
        
    def _execute_many(self, query, data):
        try:
            return self.db_cursor.executemany(query, data)
        except Exception as e:
            raise Exception("Error in sqlite_tools\n" + str(e))
        

def _connect_or_create(db_file_name):
    return sqlite3.connect(db_file_name)