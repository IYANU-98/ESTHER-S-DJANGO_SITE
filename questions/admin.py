from django.contrib import admin
from .models import PastQuestion

### This line registers your question table into the admin dashboard interface

admin.site.register(PastQuestion)