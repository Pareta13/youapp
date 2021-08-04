from django.urls import path

from . import views
app_name = "app"
urlpatterns = [
    # ex: /app/
    path('video/<str:keyword>/',views.Videolist,name='video_list'),
    path('delete/<int:pk>',views.video_delete,name='video_delete'),
    path('', views.get_keyword, name='get_keyword'),
    # # ex: /app/keyword/
    # path('<str:keyword>/<int:count>/', views.getvideo, name='video_detail'),
    # # path('<str:keyword>/channel/',views.get_video_channel,name='video-channel')
    path('csv/<str:keyword>', views.csv_view, name='get_csv_file'),
    path('<str:keyword>/delete',views.keyword_delete,name='keyword_delete')
]
