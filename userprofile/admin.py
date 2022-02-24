from django.contrib import admin

# Register your models here.

from .models import User, Pet, Wallet


admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Wallet)
