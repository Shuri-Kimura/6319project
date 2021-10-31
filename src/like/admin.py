from django.contrib import admin
from django.contrib.admin.decorators import register
from src.users.models import Cfavos, Tfavos
# Register your models here.

admin.site,register(Cfavos)
admin.site,register(Tfavos)

