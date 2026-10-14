from django.contrib import admin
from django.contrib import admin
from .models import Country, City,Post, NewsFeed


# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Post)
admin.site.register(NewsFeed)