from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def home(request):
    print('Llamada a la pagina principal')
    return render(request,'index.html')

def signup(request):

    if request.method == 'GET':
        print("Solicitud del formulario Signup")
        return render(request,'signup.html', {
        'form': UserCreationForm
        })
    else:
        print("Obteniendo datos")
        if request.POST['password1'] == request.POST['password2']:
            try:
                #Register user
                user = User.objects.create_user(username=request.POS['username'],
                pasword=request.POST['password1'])
                user.save()
                return HttpResponse('User created succesfully')
            except:
                return HttpResponse('Username alredy exists')
        return HttpResponse('Password do not match')