from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.core.signals import request_finished
from django.core.signals import setting_changed
from django.db.models.signals import post_save
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model
CustomUser = get_user_model()
#from . import forms, models

from distutils.command.upload import upload
from email.policy import default
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from authentication.models import CustomUser



"""
class User(AbstractUser):
	is_admin=models.BooleanField(default=False)
	is_auditeur=models.BooleanField(default=False)
	is_sest=models.BooleanField(default=False)
	is_expertise=models.BooleanField(default=False)
	class Meta:
		swappable='AUTH_USER_MODEL'



class Books(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete= models.CASCADE)
    isbn = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null= True)
    author = models.TextField(blank=True, null= True)
    publisher = models.CharField(max_length=250)
    date_published = models.DateTimeField()
    status = models.CharField(max_length=2, choices=(('1','Active'), ('2','Inactive')), default = 1)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "List of Books"

    def __str__(self):
        return str(f"{self.isbn} - {self.title}")
"""

class Mstage(models.Model):
	name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	def __str__(self):
		return self.name



class E_stage(models.Model):
	name=models.CharField(max_length=50)
	prenom=models.CharField(max_length=50)
	email=models.CharField(max_length=100)
	arriver=models.DateTimeField(default=False)
	depart=models.DateField(default=False)
	MS=models.ForeignKey(Mstage,on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class Book(models.Model):
	titre=models.CharField(max_length=20)
	description=models.CharField(max_length=1000)
	upload_by=models.CharField(max_length=100,null=True,blank=True)
	MS=models.ForeignKey(Mstage,null=True,blank=True,on_delete=models.CASCADE)
	created_at=models.DateTimeField(default=timezone.now)
	pdf=models.FileField(upload_to='book/pdf/',null=True,blank=True)
	image=models.ImageField(upload_to='book/image/',null=True,blank=True)#cover
	def __str__(self):
		return self.titre

	def delete(self,*args,**kwargs):
		self.pdf.delete()
		self.image.delete()
		super().delete(*args,**kwargs)

# Modèles pour gérer les utilisateurs et les discussions
class Discussion(models.Model):
    titre = models.CharField(max_length=200)

    def __str__(self):
        return self.titre

class Message(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='messages')
    auteur = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.auteur.username} - {self.date_creation}"

#gestion des Conges
class TypeConge(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Conge(models.Model):
    type_conge = models.ForeignKey(TypeConge, on_delete=models.CASCADE)
    demandeur = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    motif = models.TextField()

    def __str__(self):
        return f"{self.type_conge} - {self.demandeur.username}"










class adminHod(models.Model):
	id=models.AutoField(primary_key=True)
	#admin=models.OneToOneField(CostumerUser,on_delete=models.CASCADE)
	update_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()

class personnels(models.Model):
	id=models.AutoField(primary_key=True)
	#admin=models.OneToOneField(CostumerUser,on_delete=models.CASCADE)
	address=models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()



class documents(models.Model):
	id=models.AutoField(primary_key=True)
	document_name=models.CharField(max_length=255)
	created_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()

class communiquers(models.Model):
	id=models.AutoField(primary_key=True)
	communiquer_name=models.CharField(max_length=255)
	document_id=models.ForeignKey(documents,on_delete=models.CASCADE)
	#ajout d un champ personnel dans le model de communique et liaison a l aid de la cle
	personnels_id=models.ForeignKey(personnels,on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class employes(models.Model):
	id=models.AutoField(primary_key=True)
	#admin=models.OneToOneField(CostumerUser,on_delete=models.CASCADE)
	gender=models.CharField(max_length=255)
	profile_pic=models.FileField()
	adress=models.TextField()
	session_start_year=models.DateField()
	session_end_year=models.DateField()
	document_id=models.ForeignKey(documents,on_delete=models.DO_NOTHING)
	created_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class Attendance(models.Model):
	id=models.AutoField(primary_key=True)
	communiquer_id=models.ForeignKey(communiquers,on_delete=models.DO_NOTHING)
	attendance_date=models.DateTimeField(auto_now_add=True)
	created_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class AttendanceReport(models.Model):
	id=models.AutoField(primary_key=True)
	Employé_id=models.ForeignKey(employes,on_delete=models.DO_NOTHING)
	attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)
	status=models.BooleanField(default=False)
	created_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class leaveReportEmploye(models.Model):
	id=models.AutoField(primary_key=True)
	Employé_id=models.ForeignKey(employes,on_delete=models.CASCADE)
	leave_date=models.CharField(max_length=255)
	leave_message=models.TextField()
	leave_status=models.BooleanField(default=False)
	created_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class leaveReportPersonnel(models.Model):
	id=models.AutoField(primary_key=True)
	personnel_id=models.ForeignKey(personnels,on_delete=models.CASCADE)
	leave_date=models.CharField(max_length=255)
	leave_message=models.TextField()
	leave_status=models.BooleanField(default=False)
	created_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()

class FeedBackEmploye(models.Model):
	id=models.AutoField(primary_key=True)
	Employé_id=models.ForeignKey(employes,on_delete=models.CASCADE)
	feedback=models.TextField()
	feedback_reply=models.TextField()
	leave_status=models.BooleanField(default=False)
	created_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()

class FeedBackReportPersonnel(models.Model):
	id=models.AutoField(primary_key=True)
	personnel_id=models.ForeignKey(personnels,on_delete=models.CASCADE)
	feedback=models.TextField()
	feedback_reply=models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class NotificationEmploye(models.Model):
	id=models.AutoField(primary_key=True)
	Employé_id=models.ForeignKey(employes,on_delete=models.CASCADE)
	message=models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class NotificationPersonnel(models.Model):
	id=models.AutoField(primary_key=True)
	personnel_id=models.ForeignKey(personnels,on_delete=models.CASCADE)
	message=models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()



#@receiver(post_save,sender=CostumerUser)
def create_user_profile(sender,instance,created,**kwargs):
	if created:
		if instance.user_type==1:
			adminHod.objects.create(admin=instance)

		if instance.user_type==2:
			personnels.objects.create(admin=instance)

		if instance.user_type==3:
			employes.objects.create(admin=instance)


#@receiver(post_save,sender=CostumerUser)
def save_user_profile(sender,instance,**kwargs):
	if instance.user_type==1:
		instance.adminhod.save()
	if instance.user_type==2:
		instance.personnels.save()
	if instance.user_type==3:
		instance.personnels.save()
