from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('',views.post_list_infa, name='post_list_infa'),
    path('',views.post_listt_Fiza, name='post_list_Fiza'),
]
