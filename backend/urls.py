from django.urls import include, path
from rest_framework import routers
from backendapp.views import views

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('', views.home, name='home'),
]