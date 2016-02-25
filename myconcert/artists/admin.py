from django.contrib import admin

# Register your models here.

from .models import Artist

class ArtistAdmin(admin.ModelAdmin):
    model = Artist
    list_display = ("name", )
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Artist, ArtistAdmin)
