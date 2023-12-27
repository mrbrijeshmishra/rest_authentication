from django.contrib import admin
from .models import *


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','company_name','location']

admin.site.register(Company,CompanyAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','salary','email']

admin.site.register(Employee,EmployeeAdmin)