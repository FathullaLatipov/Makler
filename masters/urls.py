from django.urls import path
from . import views
from .views import MasterListAPIView, MasterDetailAPIView, MasterUpdateAPIView, MasterDestroyAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/v1/maklers/update', MasterUpdateAPIView)
router.register(r'api/v1/maklers/delete', MasterDestroyAPIView)

urlpatterns = [
    path('create-master/', views.MasterCreateAPIView.as_view(), name='create-master'),
    path('api/v1/maklers/', MasterListAPIView.as_view()),
    path('api/v1/maklers/<int:pk>', MasterDetailAPIView.as_view()),
]

urlpatterns += router.urls
