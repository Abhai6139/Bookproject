from django.contrib import admin

# Register your models here.
from .models import Book,AUTHOR


admin.site.register(Book)

admin.site.register(AUTHOR)