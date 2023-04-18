from django.contrib import admin

from .models import UserData, Portfolio, Contact

# Register your models here.
admin.site.register(UserData)
admin.site.register(Portfolio)
admin.site.register(Contact)