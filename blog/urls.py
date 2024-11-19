from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/' , views.index , name='index'),
    path('post/<slug>' , views.post , name = 'post'),
    path('newpost/' , views.newpost , name='new-post'),
]


