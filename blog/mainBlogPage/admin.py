from django.contrib import admin
from .models import Article #импортирую модель
# Register your models here.

admin.site.register(Article) #регистрирую модель для админки