from django.shortcuts import render

from .forms import History

import logging

def index(request):
    logger = logging.getLogger('ex02')

    if request.method == 'POST':
        form = History(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data['text'])
            form = History()
    else:
        form = History()

    history = []

    #get history from log file
    try:
        with open('ex02/logs/history.log', 'r') as f:
            history = [lines for lines in f.readlines()]
            history.reverse()
    except FileNotFoundError:
        pass
    
    return render(request, 'form.html', {'form': form, 'history': history})