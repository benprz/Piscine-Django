from . import settings
from django.urls import path
import psycopg2
from django.http import HttpResponse

def get_table_name(req_path: path):
        parse = req_path.split('/')
        if (len(parse) < 2): raise Exception(f"not know {req_path}")
        return(f"{parse[1]}_movies")

def get_db_connection() -> psycopg2.extensions.connection:
    db_config = settings.DATABASES['default']

    params = {
        "user": db_config['USER'],
        "password": db_config['PASSWORD'],
        "host": db_config['HOST'],
        "port": db_config['PORT'],
        "database": db_config['NAME']
    }

    return psycopg2.connect(**params)

def exec_sql(commands):
    if type(commands) is str:
        commands = [commands]
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        for command in commands:
            cursor.execute(command)
        value = cursor.fetchall()
        cursor.close()
        connection.commit()
        return value;
    except (Exception, psycopg2.DatabaseError) as error:
        raise Exception(error)

def init(request):

    table_name = get_table_name(request.path)
        
    req =\
    f"""
        CREATE TABLE IF NOT EXISTS {table_name}(
            title VARCHAR(64) UNIQUE NOT NULL,
            episode_nb INT PRIMARY KEY,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        );
        """

    try:
        exec_sql(req)
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse('OK')