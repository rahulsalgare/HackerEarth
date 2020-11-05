from django.contrib import admin
from .models import (UserProfile, Video, Comment, Playlist)

admin.site.register(UserProfile)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Playlist)
