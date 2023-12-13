from . import settings
from django.urls import path
import psycopg2

def get_table_name(req_path: path):
        parse = req_path.split('/')
        if (len(parse) < 2): raise Exception(f"not know {req_path}")
        return(f"{parse[1]}_movies")

def exec_sql(commands):
    db_config = settings.DATABASES['default']

    params = {
        "user": db_config['USER'],
        "password": db_config['PASSWORD'],
        "host": db_config['HOST'],
        "port": db_config['PORT'],
        "database": db_config['NAME']
    }

    if type(commands) is str:
        commands = [commands]
    try:
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        for command in commands:
            cursor.execute(command)
        cursor.close()
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        raise Exception(error)