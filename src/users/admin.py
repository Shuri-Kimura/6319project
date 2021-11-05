from django.contrib import admin
from .models import Users, Classes, Texts, Tcom, Ccom, Cevals, Uevals, Tfavos, Cfavos, Messages
# Register your models here.

admin.site.register(Users)
admin.site.register(Classes)
admin.site.register(Texts)
admin.site.register(Tcom)
admin.site.register(Ccom)
admin.site.register(Cevals)
admin.site.register(Uevals)
admin.site.register(Tfavos)
admin.site.register(Cfavos)
admin.site.register(Messages)