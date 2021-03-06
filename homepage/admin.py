from django.contrib import admin
from .models import scholarship,application_table
from import_export.admin import  ImportExportModelAdmin
from django.contrib.auth.models import  User
from .models import current_session
# Register your models here.
admin.site.register(scholarship)
admin.site.register(application_table)
admin.site.unregister(User)
admin.site.register(current_session)

@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('username','email','first_name','is_staff')