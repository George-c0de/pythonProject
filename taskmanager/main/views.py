from django.shortcuts import render, redirect

from .models import Films
from .forms import UserForm
from django.http import Http404, HttpResponseRedirect


def film(request, article_id):
    try:
        a = Films.objects.get(id=article_id)
    except:
        raise Http404("Фильм не найден")

    return render(request, 'main/film.html', {'article': a})


def index(request):
    films = Films.objects.all()
    return render(request, 'main/index.html', {'title': 'CinemaLife ', 'films': films})


def about(request, criteria):
    films = Films.objects.all()
    return render(request, 'main/about.html', {'title': 'CinemaLife ', 'films': films, 'criteria': criteria})


def create(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной '
    form = UserForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
