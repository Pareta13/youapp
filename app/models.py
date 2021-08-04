from django.db import models
from django.utils import timezone
import datetime
class Keyword(models.Model):
    keyword=models.CharField(max_length=100,default="")
    is_exported=models.BooleanField(default=False)

    def __str__(self):
        return self.keyword


class Channel(models.Model):
    keyword=models.ForeignKey(Keyword,on_delete=models.CASCADE,null=True)
    channel_id = models.CharField(max_length=20,blank=True)
    channel_name = models.CharField(max_length=200,blank=True)
    channel_link = models.URLField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=200,blank=True)
    total_view_count = models.IntegerField(blank=True, null=True)
    subscriber = models.IntegerField(blank=True, null=True)
    total_video_count = models.IntegerField(blank=True, null=True)
    instagram_handle=models.URLField(max_length=200,blank=True,null=True)
    twitter_handle=models.URLField(max_length=200,blank=True,null=True)
    facebook_handle=models.URLField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.channel_name


class Video(models.Model):
    keyword=models.ForeignKey(Keyword,on_delete=models.CASCADE,null=True)
    channel=models.ForeignKey(Channel,on_delete=models.CASCADE,null=True)
    video_id = models.CharField(max_length=20,blank=True)
    video_link = models.URLField(max_length=200,blank=True)
    video_title = models.CharField(max_length=200, blank=True)
    published_at = models.CharField(max_length=12,blank=True)
    Views = models.IntegerField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    dislikes = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.video_title

    def Video_delete(self):
        self.delete()

    def is_video_data(self):
        if self.Views:
            return True
        else:
            False


