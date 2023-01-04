from django.urls import path
# MebelCategoryListAPIView
# MebelListAPIView
from mebel.views import MebelCategoryListAPIView, MebelListAPIView

urlpatterns = [
    path('api/v1/mebel-categories/', MebelCategoryListAPIView.as_view()),
    path('api/v1/mebels/', MebelListAPIView.as_view()),
]
