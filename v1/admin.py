from django.contrib import admin
from .models import Questions
from .models import Answers
# Register your models here.

admin.site.register(Questions)
admin.site.register(Answers)
