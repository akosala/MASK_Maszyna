from django.contrib import admin
from .models import ZUS,US,Kontrah
from django.contrib.admin import site
import adminactions.actions as actions
admin.site.register(ZUS)
admin.site.register(US)
admin.site.register(Kontrah)
actions.add_to_site(site)
# Register your models here.
