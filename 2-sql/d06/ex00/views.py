from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
import d06.helper as helper

# Create your views here.
def init(request):

    table_name = helper.get_table_name(request.path)
        
    commands = [
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
    ]

    helper.exec_sql(commands)

    return HttpResponse('OK')