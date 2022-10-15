"""makler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from masters.views import MasterListAPIView, MasterDetailAPIView, MasterAddCreateAPIView, MasterUpdateAPIView, \
    MasterDestroyAPIView
from store.views import StoreModelAPIView
from .yasg import urlpatterns as doc_urls
from rest_framework.routers import DefaultRouter

from products.views import CategoryListAPIView, HouseListAPIView, AmenitiesListAPIView, \
    HouseDetailAPIView, HouseFavListAPIView, HouseAddCreateAPIView

router = DefaultRouter()
router.register(r'api/v1/maklers/create', MasterAddCreateAPIView)
router.register(r'api/v1/maklers/update', MasterUpdateAPIView)
router.register(r'api/v1/maklers/delete', MasterDestroyAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/categories/', CategoryListAPIView.as_view()),
    path('api/v1/houses/', HouseListAPIView.as_view()),
    path('api/v1/houses/create', HouseAddCreateAPIView.as_view()),
    path('api/v1/houses/<int:pk>', HouseDetailAPIView.as_view()),
    path('api/v1/amenities/', AmenitiesListAPIView.as_view()),
    path('api/v1/maklers/', MasterListAPIView.as_view()),
    # path('api/v1/maklers/create', MasterAddCreateAPIView.as_view()),
    path('api/v1/maklers/<int:pk>', MasterDetailAPIView.as_view()),
    path('api/v1/store/', StoreModelAPIView.as_view()),
    path('api/v1/fav/', HouseFavListAPIView.as_view()),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/users/', include('user.urls')),
]

urlpatterns += doc_urls
urlpatterns += router.urls
