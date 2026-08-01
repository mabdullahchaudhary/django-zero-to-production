

from django.contrib import admin
from .models import UserProfile,Employee,UserSettings


admin.site.register(UserProfile)
admin.site.register(Employee)
admin.site.register(UserSettings)