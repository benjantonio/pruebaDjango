from django.contrib import admin

# Register your models here.

from .models import Maquina, Repuesto

admin.site.register(Maquina)
admin.site.register(Repuesto)
