from django.urls import path

from products.views import GetHouseFavListAPIView
from . import views
from .views import MasterListAPIView, MasterDetailAPIView, MasterUpdateAPIView, MasterDestroyAPIView, \
    MasterCreateAPIView, SearchMasterListAPIView, RandomMasterListAPIView, MasterUserWishlistModelView, \
    GetMasterFavListAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/v1/maklers/update', MasterUpdateAPIView)
router.register(r'api/v1/maklers/delete', MasterDestroyAPIView)
router.register(r'api/v1/maklers/create', MasterCreateAPIView)
router.register(r'api/v1/maklers/wishlist-maklers', MasterUserWishlistModelView)

urlpatterns = [
    path('api/v1/maklers/', MasterListAPIView.as_view(), name='create-masters'),
    path('api/v1/maklers/get-wishlist-masters', GetMasterFavListAPIView.as_view(), name='wishlist-masters'),
    path('api/v1/maklers/popular', RandomMasterListAPIView.as_view(), name='popular-masters'),
    path('api/v1/maklers/search/', SearchMasterListAPIView.as_view(), name='search-masters'),
    path('api/v1/maklers/<int:pk>', MasterDetailAPIView.as_view()),
]

urlpatterns += router.urls
