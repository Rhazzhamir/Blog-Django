from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.index , name='index'),
    path('newpost/' , views.newpost , name='new-post'),
    path('<slug:slug>/' , views.post , name = 'post'),
    path('edit/<slug:slug>/' , views.editpost , name='edit-post'),
    path('delete/<slug:slug>/' , views.deletepost , name='delete-post'),
    path('comments/' , views.comments , name='comments' ),

]


