
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('apropos/', views.about, name='apropos'),
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('tableau_board/', views.tableau_board, name='tableau_board'),
    path('cours/', views.cours, name='cours'),
]
