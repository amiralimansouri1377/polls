from django.contrib import admin
from .models import *

# Register your models here.
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("choice_text", "question")


admin.site.register(Question)
admin.site.register(Choice, ChoiceAdmin)