from django.contrib import admin
from django.urls import path
from baiboly.views import *
from fihirana.views import *
from useraccount.views import *
from lesona.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home,name='home'),
    path("Welcome/", index,name='index'),

    path("Login/", Appsignin,name='App_signin'),
    path("S'enregistrer/", Appsignup,name='App_signup'),
    path("Deconnexion/", Appsignout,name='App_signout'),

    path("user profil/",User_profils,name='profil_utilisateur'),

    path('telecharger BD/', telecharge_fichier, name='telecharger_BD'),

    path('fihirana/', index_fihirana, name='Home_fihirana'),
    path('fihirana voalohany/', fihiranaVoalohany.fihirana_1_list, name='fihirana_1_list'),
    path('fihirana faharoa/', fihiranaFaharoa.fihirana_2_list, name='fihirana_2_list'),
    path('Fihirana fanampiny/', fihiranaFanampiny.fihirana_ajout_list, name='fihirana_ajout_list'),

    #'''Fihirana voalohany'''
    path('Mijery fihirana voalohany/<int:laharana>/', fihiranaVoalohany.fihirana_1_view, name='fihirana_1_view'),
    path('Fanintsiana Fihirana voalohany/<int:laharana>/<str:titre>/', fihiranaVoalohany.fihirana_1_mod, name='fihirana_1_mod'),

    #Fihirana faharoa
    path('Mijery fihirana Faharoa/<int:laharana>/', fihiranaFaharoa.fihirana_2_view, name='fihirana_2_view'),
    path('Fanintsiana Fihirana Faharoa/<int:laharana>/<str:titre>/', fihiranaFaharoa.fihirana_2_mod, name='modfihirana_2_mod'),
    #Fihirana fanampiny



    #'''Mampiditra hira'''
    path('Fampidirana hira/', fihiranaFanampiny.fihirana_ajout_sauvegarde, name='fihirana_ajout_sauvegarde'),
    path('fanovana hira nampidirina/<int:id>/', fihiranaFanampiny.fihirana_ajout_modif, name='fihirana_ajout_mod'),
    path('Mijery Fihirana fanampiny/<int:id>/', fihiranaFanampiny.fihirana_ajout_view, name='fihirana_ajout_view'),

    #path('Fampidirana hira/', fihirana_conf_visualisation, name='mampiditra_hira'),

    path('baiboly/', baibl, name='Home_baiboly'),
    path('boky manontolo/<str:bble>/', view_all_content, name='view_all_content'),
    
    #LESONA
    path('Fampianarana/', indexLesona, name='indexLesona'),
    path('Lesona/', listLesona, name='listLesona'),
    path('Mijerylesona/<int:title>/', ajoutContent, name='ajoutContentLesona'),
    path('Mijery lesona/<int:title>/', viewContent, name='viewContentLesona'),
    
    
    
    
]
