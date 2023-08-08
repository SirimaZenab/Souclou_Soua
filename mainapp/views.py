from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import ConnexionForm
from .forms import InscriptionForm, CreationForm
from django.contrib.auth.models import User



# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {})

def about(request):
    return render(request, 'mainapp/about.html', {})

def connexion(request):
    if request.method == 'GET':
        form = ConnexionForm(request.POST)
        return render(request, 'mainapp/connexion.html', {'form':form})
    elif request.method == "POST" :
        email = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        if user.is_authenticated :
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('ca ne marche pas!')


def deconnexion(request):
    logout(request)
    return redirect('home')

def inscription(request):
    if request.method == 'POST':
        form_inscription = InscriptionForm(request.POST)
        form_user = CreationForm(request.POST)
        if form_inscription.is_valid() :
            if form_user.is_valid() :
                user = form_user.save()
                inscription = form_inscription.save(commit = False)
                inscription.user = user
                inscription.save()
                login(request, user)

                messages.success(request, 'Votre compte a ete cree avec success')
                return redirect('connexion')
            else :
                context = {
                    'form_inscription': form_inscription,
                    'form_user': form_user,
                    'action_url': reverse('inscription')  # Générer l'URL pour l'action du formulaire
                }
                return render(request, 'mainapp/inscription.html',context)
        else :
            return render(request, "Pas bon")
            
    else:
        form_inscription = InscriptionForm()
        form_user = CreationForm()

    context = {
        'form_inscription': form_inscription,
        'form_user': form_user,
        'action_url': reverse('inscription')  # Générer l'URL pour l'action du formulaire
    }
    return render(request, 'mainapp/inscription.html', context)


def service(request):
    return render(request, 'mainapp/services.html')

def contact(request):
    return render(request, 'mainapp/contact.html')

def tableau_board(request):
    return render(request, 'mainapp/tableau_board.html')

def cours(request):
    return render(request, 'mainapp/cours.html')


