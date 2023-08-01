from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group,Permission
from django.dispatch import receiver
from django.core.signals import request_finished
from django.core.signals import setting_changed
from django.db.models.signals import post_save
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
#CustomUser = get_user_model()



class CustomUser(AbstractUser):
    photo_de_profile = models.ImageField(upload_to='profile_photos/',verbose_name='photo de profil',default='default.jpg')
    #is_on_leave = models.BooleanField(default=False)
    #avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
	 # Utilisation de related_name pour éviter les conflits de noms avec les groupes et permissions
    custom_groups = models.ManyToManyField(Group, related_name='custom_users')
    custom_user_permissions = models.ManyToManyField(Permission, related_name='custom_users')
    def __str__(self):
        return self.username

# Tâche planifiée pour supprimer les comptes fantômes (comptes inactifs)
def delete_ghost_accounts():
    # Récupérer la date actuelle
    now = timezone.now()
    # Calculer la date de seuil pour la suppression des comptes inactifs
    threshold_date = now - timedelta(days=ACCOUNT_DELETE_DELAY)
    # Récupérer les utilisateurs inactifs
    inactif_users = CustomUser.objects.filter(is_active=True, last_login__lt=threshold_date)
    # Supprimer les utilisateurs inactifs
    for user in inactif_users:
        user.delete()

"""
class User(AbstractUser):
	is_admin=models.BooleanField(default=False)
	is_auditeur=models.BooleanField(default=False)
	is_sest=models.BooleanField(default=False)
	is_expertise=models.BooleanField(default=False)
	class Meta:
		swappable='AUTH_USER_MODEL'
"""
"""
# Modèles pour gérer les utilisateurs et les discussions
class Discussion(models.Model):
    titre = models.CharField(max_length=200)

class Message(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='messages')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(default = timezone.now)
"""
