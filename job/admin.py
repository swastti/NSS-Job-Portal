# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(StudentUser)
admin.site.register(Recruiter)
admin.site.register(Job)
admin.site.register(JobD)
admin.site.register(Apply)
