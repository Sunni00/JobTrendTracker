import pyodbc
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


SERVER = 'example'
DATABASE = 'example'
USERNAME = 'example'
PASSWORD = 'example'


def connecting_to_database(link):

    try:
        a = link

        # Creating connection 
        connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

        # Use the pyodbc.connect function to connect to a SQL database.
        conn = pyodbc.connect(connectionString)


        cursor = conn.cursor()
        cursor.execute(
            '''
            insert into links
            values (?)
            ''',
            (a,)
        )
        print('successfully inserted', a)

        cursor.commit()
        cursor.close()

        return True, 'success database'

    except Exception as er:
        return False

