from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User,Candidate

class UserAdmin(BaseUserAdmin):
 add_fieldsets = (
  (None,{
   'fields':('email','username','is_admin','is_candidate','password1','password2')
  }),('Permissions',{
   'fields':('is_superuser','is_staff')
  })
 )
 fieldsets=(
  (None,{
   'fields':('email','username','is_admin','is_candidate','password')
  }),('Permissions',{
   'fields':('is_superuser','is_staff')
  })
 )
 list_display = ['email','username','is_admin','is_candidate']
 search_fields = ('email','username')
 ordering=('email',)

admin.site.register(User,UserAdmin)
admin.site.unregister(Group)
admin.site.register(Candidate)