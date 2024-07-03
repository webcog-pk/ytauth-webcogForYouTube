from django.contrib import admin
from core.models import CustomProfiles
# Register your models here.

@admin.register(CustomProfiles)
class AdminCustomProfile(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email','is_active']

