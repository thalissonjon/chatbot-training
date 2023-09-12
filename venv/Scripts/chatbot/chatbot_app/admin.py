from django.contrib import admin
from .models import *

# Register your models here.
class optionsAdmin(admin.ModelAdmin):
    list_display = ['options']
admin.site.register(userMsg, optionsAdmin)

class respAdmin(admin.ModelAdmin):
    list_display = ['msg', 'resp']
admin.site.register(botMsg, respAdmin)