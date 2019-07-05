from django.contrib import admin

from .models import IdClient

# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom', 'telephone')
    list_filter = ('nom',)
    search_fields = ['nom','prenom']


admin.site.register(IdClient, InfoAdmin)

