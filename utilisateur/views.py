from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import Stagiaire,maitreStage,BookForm
from .models import E_stage,Mstage,Book,Discussion, Message,Conge, TypeConge
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import CreateView,DetailView,DeleteView,UpdateView,ListView
from django.contrib.auth.decorators import login_required

#from utilisateur import forms



@login_required
def LT(request):
	return render(request,'utilisateur/LT.html')
@login_required
def sest(request):
	return render(request,'utilisateur/sest.html')
@login_required
def demopage(request):
	return render(request,'utilisateur/demopage.html')
#admin
@login_required
def home(request):
	return render(request,'utilisateur/home.html')

@login_required
def indexs(request):
	return render(request,'utilisateur/index.html')


@login_required
def M_stage(request):
	form=()
	if request.method=='POST':
		form=maitreStage(request.POST)
		if form.is_valid():
			nom=form.cleaned_data['name']
			prenom=form.cleaned_data['last_name']
			email=form.cleaned_data['email']
			register=Mstage(name=nom,last_name=prenom,email=email)
			if User.objects.filter(email=email):
				messages.error(request,'cet email existe deja')
				return redirect('M_stage')
			register.save()
			form=maitreStage()
			return redirect('afficher_encr')
	else:
		form=maitreStage()
	return render(request,'utilisateur/Mstage.html',{'form':form})



#les affichage des encadreurs
@login_required
def afficher_encr(request):
	afficher_encr= Mstage.objects.all()
	return render(request,'utilisateur/afficher_encr.html',{'afficher_encr':afficher_encr})

@login_required
def modifier_encr(request,id):
	if request.method=='POST':
		p=Mstage.objects.get(pk=id)
		form=maitreStage(request.POST,instance=p)
		if form.is_valid():
			form.save()
	else:
		p=Mstage.objects.get(pk=id)
		form=maitreStage(instance=p)
	return render(request,'utilisateur/modifier_encr.html',{'form':form})

@login_required
def ajouter(request):
	form=Stagiaire()
	if request.method=='POST':
		form=Stagiaire(request.POST)
		if form.is_valid():
			nom=form.cleaned_data['name']
			prenom=form.cleaned_data['prenom']
			mail=form.cleaned_data['email']
			MS=form.cleaned_data['MS']
			#date_arriver=form.cleaned_data['date_arriver']
			#date_depart=form.cleaned_data['date_depart']
			arriver=form.cleaned_data.get('arriver ')
			depart=form.cleaned_data.get('depart')
			register=E_stage(name=nom,prenom=prenom,email=mail,MS=MS)
			register.save()
			form=Stagiaire()
			return redirect('afficher')
	else:
		form=Stagiaire()
	return render(request,'utilisateur/ajouter.html',{'form':form})
@login_required
def modifier(request,id):
	if request.method=='POST':
		p=E_stage.objects.get(pk=id)
		form=Stagiaire(request.POST,instance=p)
		if form.is_valid():
			form.save()
	else:
		p=E_stage.objects.get(pk=id)
		form=Stagiaire(instance=p)
	return render(request,'utilisateur/modifier.html',{'form':form})



@login_required
def afficher(request,*args,**kwargs):
	utilisateur=E_stage.objects.all()
	if request.method=='GET':
		name=request.GET.get('recherche')
		if name is not None:
			utilisateurt=E_stage.objects.filter(name=name)
	contex={
	'utilisateur':utilisateur,
	}
	return render(request,'utilisateur/afficher.html',contex)
#archivage des document
def list_documents(request):
    documents = Book.objects.all()
    return render(request, 'utilisateur/list_documents.html', {'documents': documents})

def ajouter_document(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_documents')
    else:
        form = BookForm()
    return render(request, 'utilisateur/ajouter_document.html', {'form': form})

def lire_document(request, document_id):
    document = Book.objects.get(id=document_id)
    return render(request, 'utilisateur/lire_document.html', {'document': document})

@login_required
def demopage(request):
	return render(request,'utilisateur/demopage.html')

def delete_data(request,id):
	if request.method=='POST':
		p=E_stage.objects.get(pk=id)
		p.delete()
		return HttpResponseRedirect('delete_data')
	return renderafficher(request,'utilisateur/afficher.html')



def ajouter_discussion(request):
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            # Si le formulaire est valide, sauvegardons la nouvelle discussion dans la base de données
            discussion = form.save()  # Cela enregistre le nouveau modèle Discussion
            return redirect('detail_discussion', discussion_id=discussion.id)
    else:
        # Si c'est une requête GET, nous allons afficher le formulaire vide
        form = DiscussionForm()
    return render(request, 'ajouter_discussion.html', {'form': form})


def liste_discussions(request):
    discussions = Discussion.objects.all()
    return render(request, 'utilisateur/liste_discussions.html', {'discussions': discussions})

def detail_discussion(request,discussion_id):
    discussion = Discussion.objects.get(pk=discussion_id)
    messages = discussion.messages.all()
    return render(request, 'utilisateur/detail_discussion.html', {'discussion': discussion, 'messages': messages})


@login_required
def liste_conges(request):
    conges = Conge.objects.filter(demandeur=request.user)
    return render(request, 'utilisateur/liste_conges.html', {'conges': conges})


@login_required
def soumettre_conge(request):
    types_conge = TypeConge.objects.all()
    if request.method == 'POST':
        type_conge_id = request.POST.get('type_conge')
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')
        motif = request.POST.get('motif')

        # Validation des données
        if type_conge_id and date_debut and date_fin and motif:
            type_conge = TypeConge.objects.get(id=type_conge_id)

            # Créer un nouvel objet Conge avec les données soumises
            conge = Conge.objects.create(
                type_conge=type_conge,
                demandeur=request.user,
                date_debut=date_debut,
                date_fin=date_fin,
                motif=motif
            )
            # Enregistrement du congé dans la base de données
            conge.save()

            # Changer le statut de l'utilisateur en congé (actif/inactif)
            CustomUser = get_user_model()
            user = CustomUser.objects.get(pk=request.user.pk)
            user.is_on_leave = True
            user.save()

            # Rediriger vers la page de liste des congés après soumission réussie
            return redirect('liste_conges')

    return render(request, 'utilisateur/soumettre_conge.html', {'types_conge': types_conge})
