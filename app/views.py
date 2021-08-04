from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from pprint import pprint
from pyyoutube import Api
from youtubesearchpython.__future__ import *
from youtubesearchpython import VideosSearch,CustomSearch
from .forms import youtube

import re
import csv
from app.models import Video,Keyword,Channel
DEVELOPER_KEY = "AIzaSyBoLPDCZVlgRLYxUeiEuPJpd-2nOtOm8Gw"
api = Api(api_key=DEVELOPER_KEY)



def get_data(keyword,sort):
    x=Keyword.objects.create(keyword=keyword)
    x.save()
    # videosSearch = VideosSearch(keyword, limit=20, language='en', region='US')
    videosSearch=CustomSearch(keyword,sort)
    videosResult = videosSearch.result()
    for i in videosResult['result']:
        channel_id=i['channel']['id']
        channel_instance =Channel.objects.filter(channel_id=channel_id).first()
        channel_name=i['channel']['name']
        channel_link=i['channel']['link']
        if channel_instance is None:
            channel= Channel.objects.create(
                keyword=x,
                channel_id=channel_id,
                channel_name=channel_name,
                channel_link=channel_link,
                email=''
            )
            channel.save()
            Video.objects.create(
                channel=channel,
                keyword=x,
                video_title=i['title'],
                video_id=i['id'],
                video_link=i['link']

            ).save()

        else:
            Video.objects.create(
                channel=channel_instance,
                keyword=x,
                video_title=i['title'],
                video_id=i['id'],
                video_link=i['link']
            ).save()

def get_channel_data(keyword):
    channels= Keyword.objects.get(keyword=keyword).channel_set.all()
    for i in channels:
        id=i.channel_id
        channel=api.get_channel_info(channel_id=id).items[0].to_dict()
        desc = channel['snippet']['localized']['description']
        try:
            email = re.findall(r'[\w\.-]+@[\w\.-]+', desc)[0]
            email=email.replace('-',"")
        except:
            email = ""
        try:
            instagram_handle=''
        except:
            instagram_handle = ''

        try:
            facebook_handle=re.findall(r'(?:(?:http|https):\/\/)?(?:www.)?facebook.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?',desc)[0]

        except:
            facebook_handle=''
        try:
            twitter_handle=''
        except:
            twitter_handle=''
        i.total_view_count= channel['statistics']['viewCount']
        i.subscriber= channel['statistics']['subscriberCount']
        i.total_video_count= channel['statistics']['videoCount']
        i.email= email
        i.instagram_handle=instagram_handle
        i.facebook_handle=facebook_handle
        i.twitter_handle=twitter_handle
        i.save()


def get_video_data(keyword):
    videos=Keyword.objects.get(keyword=keyword).video_set.all()
    for i in videos:
        id=i.video_id
        d=api.get_video_by_id(video_id=id).items[0].to_dict()
        likes = 0
        dislikes = 0
        views = 0
        comments = 0
        if 'likeCount' in d['statistics'].keys():
            likes = d['statistics']['likeCount']

        if 'dislikeCount' in d['statistics'].keys():
            dislikes = d['statistics']['dislikeCount']

        if 'viewCount' in d['statistics'].keys():
            views = d['statistics']['viewCount']

        if 'commentCount' in d['statistics'].keys():
            comments = d['statistics']['commentCount']

        date = d['snippet']['publishedAt']
        date = date[0:10]
        desc = d['snippet']['description']
        i.likes=likes
        i.dislikes=dislikes
        i.views=views
        i.comments=comments
        i.published_at=date
        i.save()

def get_keyword(request):
    if request.method=='POST':
        form=youtube(request.POST)
        print(form)
        if form.is_valid():
            keyword=form.cleaned_data['keyword']
            sort=form.cleaned_data['sort_option']
            print(sort)
            print(type(sort))
            if Keyword.objects.filter(keyword=keyword).count()==0:
                get_data(keyword,sort=sort)
            return redirect('app:video_list',keyword=keyword)

    else:
        form=youtube()
        return render(request,'app/home.html',{'form':form})


def csv_view(request,keyword):
    # Create the HttpResponse object with the appropriate CSV header.
    keyword_instance=Keyword.objects.get(keyword=keyword)
    if keyword_instance.is_exported==False:
        get_channel_data(keyword)
        get_video_data(keyword)
        keyword_instance.is_exported = True
        keyword_instance.save()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    writer = csv.writer(response)
    writer.writerow(['channel_name', 'channel_link', 'email','total_view_count','subscriber','total_video_count','video_link','video_title','published_at','Views','likes','comments','dislikes'])

    for i in keyword_instance.video_set.all():
        writer.writerow([i.channel.channel_name, i.channel.channel_link, i.channel.email,i.channel.total_view_count,i.channel.subscriber,i.channel.total_video_count,i.video_link,
                         i.video_title,i.published_at,i.Views,i.likes,i.comments,i.dislikes])
    return response

def Videolist(request,keyword):
    videos=Keyword.objects.get(keyword=keyword).video_set.all()
    return render(request,'app/index.html',{'videos':videos,'keyword':keyword})

def video_delete(request,pk):
    video=Video.objects.get(pk=pk)
    keyword=video.keyword.keyword
    channels=video.channel.video_set.count()
    if channels==1:
        video.channel.delete()
    else:
        video.delete()
    return redirect('app:video_list',keyword=keyword)

def keyword_delete(request,keyword):
    Keyword.objects.get(keyword=keyword).delete()
    return redirect('get_keyword')
