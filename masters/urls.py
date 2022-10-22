from django.urls import path
from . import views

urlpatterns = [
    path('create-master/', views.MasterCreateAPIView.as_view(), name='create-master'),
]