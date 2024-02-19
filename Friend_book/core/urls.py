from django.urls import path
from . import views
#from .views import ListThreads,CreateThread,ThreadView,CreateMessage

urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post/', views.like_post, name='like-post'),

    #path('list_users/', views.list_users, name='list_users'),
    path('message_detail/<int:user_id>/', views.message_detail, name='message_detail'),
    #path('myprofile/<str:pk>/', views.myprofile, name='myprofile'),

    #path('inbox/', ListThreads.as_view(), name='inbox'),
    #path('inbox/create_thread', CreateThread.as_view(), name='create_thread'),
    #path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    #path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),

    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
]