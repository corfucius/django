from django.contrib import admin

#bring in models from models
from .models import Posts
# Register your models here.

admin.site.register(Posts)
