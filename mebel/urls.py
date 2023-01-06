from django.urls import path
# MebelCategoryListAPIView
# MebelListAPIView
from rest_framework.routers import DefaultRouter

from mebel.views import MebelCategoryListAPIView, MebelListAPIView, MebelCreateAPIView

router = DefaultRouter()
router.register(r'api/v1/mebels/create', MebelCreateAPIView)

urlpatterns = [
    path('api/v1/mebel-categories/', MebelCategoryListAPIView.as_view()),
    path('api/v1/mebels/', MebelListAPIView.as_view()),
    path('api/v1/mebels/', MebelListAPIView.as_view()),
]

urlpatterns += router.urls
