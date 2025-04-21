from django.shortcuts import render, redirect
from .models import MovieMod
from .forms import MovieForm
from django.contrib import messages

# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')


def add(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.add_message(
                request, level=messages.SUCCESS, message='Movie Registered Successfully')
        return redirect('add')
    return render(request, 'add.html', {'form': form})


def display(request):
    data = MovieMod.objects.all()
    return render(request, 'display.html', {'data': data})
