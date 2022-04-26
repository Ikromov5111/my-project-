from atexit import register
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Worker)
# admin.site.register(Article)
admin.site.register(Room)
admin.site.register(Ijara)