from django.shortcuts import render

# Create your views here.
def colors(request):
    step = 256 / 50
    context = {
        "range": [
            int(i * step) for i in range(50)
        ]
    }
    return render(request, 'colors.html', context)