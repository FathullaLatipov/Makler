from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

from .views import StoreAddCreateAPIView, StoreUpdateAPIView, StoreDestroyAPIView, StoreModelAPIView, \
    StoreDetailAPIView, SearchStoreModelAPIView, RandomStoreModelAPIView, UseForModelSerializerAPIView, \
    HowStoreServiceModelSerializerAPIView

router = DefaultRouter()
router.register(r'api/v1/store/create', StoreAddCreateAPIView)
router.register(r'api/v1/store/delete', StoreDestroyAPIView)

urlpatterns = [
    path('api/v1/store/', StoreModelAPIView.as_view()),
    path('api/v1/store/use_for', UseForModelSerializerAPIView.as_view()),
    path('api/v1/store/how_store', HowStoreServiceModelSerializerAPIView.as_view()),
    path('api/v1/store/update/<int:pk>', StoreUpdateAPIView.as_view()),
    path('api/v1/store/popular', RandomStoreModelAPIView.as_view()),
    path('api/v1/store/search', SearchStoreModelAPIView.as_view()),
    path('api/v1/store/<int:pk>', StoreDetailAPIView.as_view()),
]

urlpatterns += router.urls
