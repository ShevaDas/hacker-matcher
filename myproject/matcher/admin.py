from django.contrib import admin
from matcher.models import Hacker

# Register your models here.

admin.site.register(Hacker)

class HackerAdmin(admin.ModelAdmin):
	list_display = ('id', 'full_name', 'gender', 'skill', 'looking_for')
