from django.contrib import admin
from .models import Rentals,User,Properties

admin.site.register(User)
admin.site.register(Rentals)
admin.site.register(Properties)

# Register your models here.
