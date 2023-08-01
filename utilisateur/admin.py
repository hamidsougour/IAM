from django.contrib import admin
"""from utilisateur.models import Users
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
	list_display=('id','name','email','password')
#admin.site.register(Users,UserAdmin)
"""
from .models import E_stage,Book,Mstage,personnels,documents,communiquers,employes,Attendance,AttendanceReport,leaveReportEmploye,FeedBackEmploye,leaveReportPersonnel,NotificationEmploye,FeedBackReportPersonnel,NotificationPersonnel,adminHod,Discussion,Message,TypeConge

from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
	pass
admin.site.register(Discussion)
admin.site.register(Message)
admin.site.register(E_stage)
admin.site.register(Mstage)
admin.site.register(Book)
admin.site.register(personnels)
admin.site.register(documents)
admin.site.register(communiquers)
admin.site.register(employes)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(leaveReportEmploye)
admin.site.register(leaveReportPersonnel)
admin.site.register(FeedBackEmploye)
admin.site.register(FeedBackReportPersonnel)
admin.site.register(NotificationEmploye)
admin.site.register(NotificationPersonnel)
admin.site.register(adminHod)
admin.site.register(TypeConge)
#admin.site.register(admin_user)
