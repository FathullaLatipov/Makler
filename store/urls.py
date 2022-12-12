from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

from .views import StoreAddCreateAPIView, StoreUpdateAPIView, StoreDestroyAPIView, StoreModelAPIView, \
    StoreDetailAPIView, SearchStoreModelAPIView

router = DefaultRouter()
router.register(r'api/v1/store/create', StoreAddCreateAPIView)
router.register(r'api/v1/store/update', StoreUpdateAPIView)
router.register(r'api/v1/store/delete', StoreDestroyAPIView)

urlpatterns = [
    path('api/v1/store/', StoreModelAPIView.as_view()),
    path('api/v1/store/search', SearchStoreModelAPIView.as_view()),
    path('api/v1/store/<int:pk>', StoreDetailAPIView.as_view()),
]

urlpatterns += router.urls
