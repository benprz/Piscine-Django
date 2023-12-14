from django.shortcuts import render
from d06.globals import exec_sql, get_table_name
from django.http import HttpResponse, HttpRequest
from .forms import RemoveForm

def populate(request):
    movies = [
        {
            'episode_nb': 1,
            'title': 'The Phantom Menace',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '1999-05-19'
        },
        {
            'episode_nb': 2,
            'title': 'Attack of the Clones',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2002-05-16'
        },
        {
            'episode_nb': 3,
            'title': 'Revenge of the Sith',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2005-05-19'
        },
        {
            'episode_nb': 4,
            'title': 'A New Hope',
            'director': 'George Lucas',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1977-05-25'
        },
        {
            'episode_nb': 5,
            'title': 'The Empire Strikes Back',
            'director': 'Irvin Kershner',
            'producer': 'Gary Kutz, Rick McCallum',
            'release_date': '1980-05-17'
        },
        {
            'episode_nb': 6,
            'title': 'Return of the Jedi',
            'director': 'Richard Marquand',
            'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
            'release_date': '1983-05-25'
        },
        {
            'episode_nb': 7,
            'title': 'The Force Awakens',
            'director': 'J. J. Abrams',
            'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
            'release_date': '2015-12-11'
        }
    ]
    http_response = ""
    table_name = get_table_name(request.path)
    for movie in movies:
        commands = [
            f"""
            INSERT INTO {table_name} (episode_nb, title, director, producer, release_date)
            VALUES ({movie['episode_nb']}, '{movie['title']}', '{movie['director']}', '{movie['producer']}', '{movie['release_date']}')
            """
        ]
        http_response += f"{movie['title']}: "
        try:
            exec_sql(commands)
            http_response += "OK<br>"
        except Exception as e: http_response += f"KO ( {e})<br>"

    return HttpResponse(http_response)

def display(request):
    table_name = get_table_name(request.path)
    commands = [
        f"""
        SELECT * FROM {table_name}
        """
    ]
    try:
        movies = exec_sql(commands, fetchall=True)
    except:
        return HttpResponse("No data available")
    if len(movies) == 0:
        return HttpResponse("No data available")
    return render(request, 'ex02/display.html', {'movies': movies})

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
    
