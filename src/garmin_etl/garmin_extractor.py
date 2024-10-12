from ..util.sqlite_tools import sqlite_tools


db = sqlite_tools("../database/garmin_data")
#confirm table exists, if not, create the table