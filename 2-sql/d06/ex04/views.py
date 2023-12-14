from django.shortcuts import render
from d06.globals import exec_sql, get_table_name
from django.http import HttpResponse, HttpRequest
from .forms import RemoveForm

# Create your views here.
def remove(request: HttpRequest):
    table_name = get_table_name(request.path)
    commands = [
        f"""
        SELECT * FROM {table_name}
        """
    ]

    try:
        if request.method == 'POST':
            title = request.POST.get('title')
            exec_sql(f"DELETE FROM {table_name} WHERE title = '{title}'")
        
        movies = exec_sql(commands, fetchall=True)
        if len(movies) == 0:
            raise
        context = {'form': RemoveForm(choices=((movie[0], movie[0]) for movie in movies))}
        return render(request, 'remove.html', context)
    except:
        return HttpResponse(f"No data available <br>")
    
