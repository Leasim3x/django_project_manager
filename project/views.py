from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponse

# Create your views here.


def home(request):
    print('Llamada a la pagina principal')
    return render(request, 'index.html')


def signup(request):

    if request.method == 'GET':
        print("Solicitud del formulario Signup")
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        print("Obteniendo datos")
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Register user
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                print(request.POST)
                user.save()
                # Cookie user
                login(request, user)
                return redirect('projects')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })


def projects(request):
    return render(request, 'projects.html')


def tasks(request):
    return render(request, 'tasks.html')
