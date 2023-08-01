from django.core import validators
from django.forms import fields
from .models import  E_stage,Mstage,Book,Discussion, Message
from django import forms
from datetime import date
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm




class Stagiaire(forms.ModelForm):
	#arriver=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
	#depart=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
	class Meta:
		model=E_stage
		fields=['name','email','prenom','arriver','depart','MS']
		widgets={
			'name':forms.TextInput(attrs={'class':'form-control'}),
			'prenom':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'arriver':forms.DateInput(attrs={'class':'form-control'}),
			'depart':forms.DateInput(attrs={'class':'form-control'}),
			'MS':forms.TextInput(attrs={'class':'form-control'})}


class maitreStage(forms.ModelForm):
	class Meta:
		model=Mstage
		fields=['name','last_name','email']
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'}),
		'last_name':forms.TextInput(attrs={'class':'form-control'}),
		'email':forms.EmailInput(attrs={'class':'form-control'})}


class BookForm(forms.ModelForm):
	class Meta:
		model=Book
		fields=['titre','description','upload_by','MS','created_at','pdf','image']




class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['titre']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['contenu']
