from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    video_title = models.CharField(max_length=50)
    video_description = models.TextField()
    published_date = models.DateField(auto_now=True)
    video_owner = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos/', null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True)

    def __str__(self):
        return self.video_title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        default='profilepic/default.png', upload_to='profilepic/', null=True, blank=True)

    cover_pic = models.ImageField(
        default='coverpic/default.jpg', upload_to='coverpic/', null=True, blank=True)

    liked_videos = models.ManyToManyField(
        Video, related_name="user_liked_videos", blank=True)

    viewed_videos = models.ManyToManyField(
        Video, related_name="user_viewed_videos", blank=True)

    saved_playlists = models.ManyToManyField('Playlist', blank=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    comment_text = models.TextField(max_length=300)
    comment_datetime = models.DateTimeField(blank=False, null=False)
    comment_owner = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    commented_video = models.ForeignKey('Video', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=50, default="new playlist")
    playlist_videos = models.ManyToManyField(Video, null=True)
    playlist_owner = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.playlist_name
