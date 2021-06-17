from django.contrib import admin
from .models import RegisteredUser, FeedItem

# Register your models here.
admin.site.register(RegisteredUser)
admin.site.register(FeedItem)