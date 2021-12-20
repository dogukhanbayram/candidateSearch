from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontend, name="frontend"),
    path('fullstack/', views.fullStack, name="fullStack"),
    path('mobiledev/', views.mobileDev, name="mobileDev"),
]
