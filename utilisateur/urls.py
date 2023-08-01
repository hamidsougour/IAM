from django.contrib import admin
from django.urls import path
from .views import ajouter,modifier,afficher,delete_data,demopage,LT,sest,home,M_stage,afficher_encr,modifier_encr,list_documents,ajouter_document,lire_document,liste_discussions,detail_discussion,liste_conges,soumettre_conge,ajouter_discussion
from .views import indexs
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
#from utilisateur import settings


urlpatterns = [
    path('indexs',indexs,name='indexs'),
    path('ajouter',ajouter,name='ajouter'),
    path('afficher',afficher,name='afficher'),


    path('operation/<int:id>/',delete_data,name='delete_data'),
    path('modifier/<int:id>/', modifier,name='modifier'),
    path('demopage/',demopage,name='demopage'),

    #les encadreurs
    path('afficher_encr/',afficher_encr,name='afficher_encr'),
    path('delete/<int:id>/',delete_data,name='delete_data'),
    path('modifier_encr/<int:id>/',modifier_encr,name='modifier_encr'),

    path('M_stage/',M_stage,name='M_stage'),


    path('LT/',LT,name='LT'),
    path('sest/',sest,name='sest'),

    #admin ou dashbord
    path('home/',home,name='home'),


    #path('modifier_encr',modifier_encr,name='modifier_encr'),

    #archivage
    path('documents/',list_documents, name='list_documents'),
    path('ajouter_document/',ajouter_document, name='ajouter_document'),
    path('documents/<int:document_id>/',lire_document, name='lire_document'),

    #url de discussion
    path('discuter/',ajouter_discussion,name='discuter'),
    path('discussions/',liste_discussions, name='liste_discussions'),
    path('discussions/<int:discussion_id>/',detail_discussion, name='detail_discussion'),
    #gestion des congés
    path('liste/',liste_conges, name='liste_conges'),
    path('soumettre/',soumettre_conge, name='soumettre_conge')

]
