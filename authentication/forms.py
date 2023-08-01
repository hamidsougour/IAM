from django import forms
from django.contrib.auth import get_user_model
from django import forms
from .models import CustomUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['photo_de_profile']

class LoginForm(forms.Form):
	username=forms.CharField(
		widget=forms.TextInput(
			attrs={
			"class":" form-control-sm mb-3"
			}
		)
	)
	password=forms.CharField(
		widget=forms.PasswordInput(
			attrs={
			"class":"form-control-sm mb-3"
			}
		)
	)



"""

class SignUpForm(UserCreationForm):
	username=forms.CharField(
		widget=forms.TextInput(
			attrs={
			"class":"form-control"
			}
		)
	)
	email=forms.CharField(
		widget=forms.TextInput(
			attrs={
			"class":"form-control"
			}
		)
	)
		password=forms.CharField(
		widget=forms.PasswordInput(
			attrs={
			"class":"form-control"
			}
		)
	)
	confirmation=forms.CharField(
		widget=forms.PasswordInput(
			attrs={
			"class":"form-control"
			}
		)
	)


	class Meta:
		model=User
		fields=['username','email','administrateur','Employé','partenaire']

"""
