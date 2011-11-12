from motaskra.models import Club
from django.contrib import admin

class ClubAdmin(admin.ModelAdmin):
    list_display = ('clubName', 'shortName','address1')

admin.site.register(Club)

