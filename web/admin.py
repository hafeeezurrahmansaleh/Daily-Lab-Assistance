from django.contrib import admin
from .models import  Announcement
from .models import Courses


# Register your models here.

admin.site.register(Courses)
admin.site.register(Announcement)
