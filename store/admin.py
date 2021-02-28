from django.contrib import admin

#untuk mengimport data yang berada di file models
from .models import *

admin.site.register(Product)
admin.site.register(Description)
