from django.contrib import admin
from . models import Record
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Record, AuthorAdmin)