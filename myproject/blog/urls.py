from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('news/',views.news),
    path('cerita/',views.cerita),
]