from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth,messages
from iam import settings
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.views.generic import CreateView,DetailView,DeleteView,UpdateView,ListView
from django import forms
from .forms import LoginForm#,UploadProfilePhotoForm#,SignUpForm
from .forms import ProfileForm
from .models import  CustomUser
#User = settings.AUTH_USER_MODEL
#from .models import User
#from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
#from django.utils.encoding import force_bytes,force_text
#from django.template.loader import render_to_string
#from django.contrib.sites.shortcuts import get_current_site
#from .token import genererToken
def loginRegister(request):
	if request.method=='POST':
		username=request.POST['username']
		firstname=request.POST['firstname']
		lastname=request.POST['lastname']
		username=request.POST['username']
		email=request.POST['email']
		password=request.POST['password']
		password1=request.POST['password1']
		if CustomUser.objects.filter(username=username):
			messages.error(request,'utilisateur existe deja')
			return redirect('loginRegister')
		if CustomUser.objects.filter(email=email):
			messages.error(request,'cet email existe deja')
			return redirect('loginRegister')
		if not password.isalnum():
			messages.error(request,'le mot de passe doit etre composer des caracteres et des chiffres')
			return redirect('loginRegister')
		if password !=password1:
			messages.error(request,'les deux mot de passe ne sont pas identique')
			return redirect('loginRegister')
		my_user =CustomUser.objects.create_user(username, email, password)
		my_user.first_name=firstname
		my_user.last_name=lastname
		my_user.save()
		messages.success(request,'successfull')
		return redirect('loginPage')
	return render(request,'authentication/loginRegister.html')


def loginPage(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		if user is not None and user.is_active:
			login(request,user)
			firstname=user.first_name
			return render(request,'authentication/index.html',{'firstname':firstname})
		else:
			messages.error(request,'identifiants invalide')
			return redirect('ajouter')
	return render(request,'authentication/loginPage.html')





def logoutUser(request):
	logout(request)
	messages.success(request,'vous etes deconnectés')
	return redirect('loginPage')




def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')  # Rediriger vers la page de confirmation
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'authentication/upload_profile_photo.html', {'form': form})

"""
def loginPage(request):
	if request.method=='POST':
		username=request.POST['user_name']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		if user is not None and user.is_active:
			auth.login(request,user)
			if user.is_admin or user.is_superuser:
				return redirect(index)
			elif user is not None and user.is_expertise:
				return redirect('dasboard')
			elif user.is_auditeur:
				return redirect('auditeur')
			else:
				return redirect('sest')
		else:
			messages.info(request,'identifiant incorrect')
			return redirect('demopage')


	return render(request,'utilisateur/m.html')
"""


def enregistrement(request):
	"""
	if request.method=='POST':
		fname=request.POST.get('fname')
		lname=request.POST.get('sname')
		name=request.POST.get('user_name')
		email=request.POST.get('email')
		password=request.POST.get('pass')
		if User.objects.filter(email=email):
			messages.error(request,'cet email existe deja')
			return redirect('enregistrement')

		if not name.isalnum():
			messages.error(request,'le nom doit etre alpha numerique')
			return redirect('enregistrement')

		new_user=User.objects.create_user(name,email,password)
		new_user.first_name=fname
		new_user.last_name=lname
		new_user.is_active=False
		messages.success(request,'vous etes connectez avec succes')
		new_user.save()

		#envoi de mail de bienvenue
		subject='bienvenue dans notre IAM'
		message='felicitation '+new_user.first_name+" "+new_user.last_name+" bienvenue dans notre systeme IAM"
		from_email=settings.EMAIL_HOST_USER
		to_list=[new_user.email]
		send_mail(subject,message,from_email,to_list,fail_silently=False)

		#envoie de mail de confirmation

		current_site=get_current_site(request)
		email_subject='confirmation de mail dans l\'IAM'
		messageConf=render_to_string('emailConf.html',{
			'name':new_user.first_name,
			'domain':current_site.domain,
			'uid':urlsafe_base64_encode(force_bytes(new_user.pk)),
			'token':genererToken.make_token(new_user)
		})
		email=EmailMessage(
			email_subject,
			messageConf,
			settings.EMAIL_HOST_USER,
			[new_user.email]
		)
		email.fail_silently=False
		email.send()
		return redirect('password')
		"""
	return render(request,'authentication/enregistrement.html',{"message":messages})
def password(request):
	"""
	if request.method=='POST':
		name=request.POST.get('uname')
		password=request.POST.get('pass')
		user=authenticate(request,name=name,password=password)
		if user is not None:
			login(request,user)
			return redirect('base')
			"""
	return render(request,'authentication/password.html',{})

"""
"""


def activate(request,uidb64,token):
	try:
		uid=force_text(urlsafe_base64_decode(uidb64))
		user=User.objects.get(pk=uid)
	except(TypeError,ValueError,OverflowError, User.DoesNotExist):
		user=None
	if user is not None and genererToken.check_token(user,token):
		user.is_active=True
		user.save()
		messages.success(request,'votre compte est activé.felicitation!!')
		return redirect('password')

	else:
		messages.error(request,'activation echoué,\n veillez ressayer svp')
		return redirect('enregistrement')

#@login_required
def index(request):
	return render(request,'authentication/index.html',{})



def base(request):
	return render(request,'authentication/base.html')




def login_view(request):
	form=LoginForm(request.POST or None)
	msg=None
	if request.method=='POST':
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(username=username,password=password)
			if user is not None and user.administrateur:
				login(request,user)
				return redirect('admin')
			elif user is not None and user.Employé:
				login(request,user)
				return redirect('base')
			elif user is not None and user.partenaire:
				login(request,user)
				return redirect('partenaire')
			#elif user is not None and user.contractuel:
				#login(request,user)
				#return redirect('contractuel')

			else:
				msg='authentification invalide'
		else:
			msg='authentification invalide'
			contex={
			'form':form,
			'msg':msg
			}
	return render(request,'authentication/login_view.html',contex)

def view_profile(request):
	args={'user':request.user}
	return render(request,'authentication/profile.html',args)


def change_password(request):
	if request.method=='POST':
		form=PasswordChangeForm(data=request.POST,user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			return redirect('profile')
		else:
			return redirect('change_password')
	form=PasswordChangeForm(user=request.user)
	args={'form':form}
	return render(request,'authentication/change_password.html',args)


#@login_required
def photo_profile(request):
	return render(request, 'authentication/photo_profile.html')
