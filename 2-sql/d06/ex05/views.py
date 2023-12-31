from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies
from .forms import RemoveForm

# Create your views here.
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
    model = Movies()
    http_response = ""
    for movie in movies:
        http_response += f"{movie['title']}: "
        try:
            model.title = movie['title']
            model.episode_nb = movie['episode_nb']
            model.director = movie['director']
            model.producer = movie['producer']
            model.release_date = movie['release_date']
            model.save()
            http_response += "OK<br>"
        except Exception as e: http_response += f"KO ( {e})<br>"
    return HttpResponse(http_response)

def display(request):
    movies = Movies.objects.all()
    if len(movies) == 0:
        return HttpResponse("No data available")
    return render(request, 'ex03/display.html', {'movies': movies})


# Create your views here.
def remove(request):
    if request.method == 'POST':
        try:
            Movies.objects.get(title=request.POST['title']).delete()
        except:
            return HttpResponse(f"No data available")
    movies = Movies.objects.all()
    choices = ((movie.title, movie.title) for movie in movies)
    context = {'form': RemoveForm(choices)}
    return render(request, 'remove.html', context)