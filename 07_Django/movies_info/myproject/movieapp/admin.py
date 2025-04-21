from django.contrib import admin
from .models import MovieMod

# Register your models here.


class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id', 'mname', 'hero', 'heroine',
                    'rdate', 'director', 'lang', 'rating']


admin.site.register(MovieMod, MoviesAdmin)
