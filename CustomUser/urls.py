from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.empty, name='empty'),
    path('home', views.home, name='home'),
    path('signup/', views.signup2, name='signup'),
    path('about/<str:usernameurl>/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('donate/', views.donate, name="donate"),
    path('displaydonate/<int:donatepage>', views.displaydonate, name="displaydonate"),
    path('editabout/', views.AboutEdit, name='editabout'),
    path('sendmessage/<int:postid>/<str:to>/<str:fromperson>/', views.sendmessage, name='sendmessage'),
    path('askquestion/', views.ask, name="askquestion"),
    path('topics/', views.topics, name="topics"),
    path('topics/<int:id>', views.topic_specific, name="topic_specific"),
    path('UpRec/', views.UpRec, name='AskForUploadRecieve'),
    path('search/',views.searchbox, name='search'),
    path('sendmsg',views.sendmsg, name='sendmsg'),
    path('reward/', views.reward, name="reward"),
    path('pdf_splitscreen/',views.pdf_split, name="pdf_split"),
    path('pdf_upload/',views.pdf_upload, name="pdf_upload"),
    path('sentmsg/', views.sentmsg, name='sentmsg'),
    path('recvmsg/', views.recvmsg, name='recvmsg'),    
]
