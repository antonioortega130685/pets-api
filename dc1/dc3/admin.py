from django.contrib import admin
from .models import Pet
# Register your models here.

class PetAdmin(admin.ModelAdmin):
    fieldsets = [
    	('User information', {'fields': ['owner']}),
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['birthday']}),
        (None, {'fields':['species']}),
    ]
    list_display = ('name', 'birthday', 'species')
    search_fields = ['name']


admin.site.register(Pet, PetAdmin)