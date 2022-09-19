from django.urls import path 
from .views import ArticleDetailview, HomeView,Postblog, Updatepost

urlpatterns = [
    # path('', views.Home, name='home')
    path('',HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailview.as_view(),name="article"),
    path('add_post/', Postblog.as_view(), name="addblog"),
    path('article/edit/<int:pk>',Updatepost.as_view(),name="updatepost"),
]
