from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('index.html', views.post_list),
    path('streaming.html', views.post_list),
    path('metaverso.html', views.post_list),
    path('museu.html', views.post_list),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
