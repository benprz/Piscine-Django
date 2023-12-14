from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies
from ex04 import RemoveForm

# Create your views here.
def remove(request):
    if request.method == 'POST':
        try:
            Movies.objects.get(title=request.POST['title']).delete()
        except:
            return HttpResponse(f"No data available")
    movies = Movies.objects.all()
    context = {'form': RemoveForm(choices=((movie[0], movie[0]) for movie in movies))}
    return render(request, 'remove.html', context)