from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index,password,enregistrement,logoutUser,activate,base,login_view,change_password,view_profile,photo_profile,loginPage,loginRegister,update_profile#,upload_profile_photo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('accueil/',page_accueil,name='accueil'),
    path('enregistrement/',enregistrement,name='enregistrement'),
    path('password/',password,name='password'),
    path('deconnecter/',logoutUser,name='logoutUser'),
    path('activate/<uidb64>/<token>',activate,name='activate'),
    path('loginPage/',loginPage,name='loginPage'),
    path('loginRegister/',loginRegister,name='loginRegister'),

    path('indexs/',index,name='index'),
    path('base/',base,name='base'),
    path('login/',login_view,name='login_view'),
    #path('register/',register,name='register'),
    path('profile/',view_profile,name='profile'),
    path('change-password/',change_password,name='change_password'),
    path('photo_profile/', photo_profile, name='users-profile'),

    #profile
    #path('upload_profile_photo/',upload_profile_photo, name='upload_profile_photo'),
    path('update_profile/',update_profile,name='update_profile'),
    #reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
