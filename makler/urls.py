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

from masters.views import MasterListAPIView, MasterDetailAPIView, MasterUpdateAPIView, \
    MasterDestroyAPIView, PostList, PostDetail
from store.views import StoreModelAPIView, StoreDetailAPIView, StoreAddCreateAPIView, StoreUpdateAPIView, \
    StoreDestroyAPIView
from user.views import UserDetail, UserList, LoginView, UserViewSet
from .yasg import urlpatterns as doc_urls
from rest_framework.routers import DefaultRouter

from products.views import CategoryListAPIView, HouseListAPIView, AmenitiesListAPIView, \
    HouseDetailAPIView, HouseFavListAPIView, HouseUpdateAPIView, HouseDestroyAPIView, \
    HouseImageAPIView, HouseArchiveListAPIView, WebAmenitiesListAPIView, HouseAddCreateAPIView, \
    WebPriceListAPIView, WebHomeCreateView, snippet_list, WebHomeListAPIView, APPHouseAddCreateAPIView

from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register('login', LoginView, 'auth')
router.register('signup', UserViewSet, 'register')
# router.register(r'api/v1/maklers/create', MasterAddCreateAPIView)
router.register(r'api/v1/maklers/update', MasterUpdateAPIView)
router.register(r'api/v1/maklers/delete', MasterDestroyAPIView)
router.register(r'api/v1/houses/create', HouseAddCreateAPIView)
router.register(r'api/v1/houses/app-create', APPHouseAddCreateAPIView)
router.register(r'api/v1/houses/update', HouseUpdateAPIView)
router.register(r'api/v1/houses/delete', HouseDestroyAPIView)
router.register(r'api/v1/store/create', StoreAddCreateAPIView)
router.register(r'api/v1/store/update', StoreUpdateAPIView)
router.register(r'web/api/v1/web-houses', WebHomeCreateView)
router.register(r'api/v1/store/delete', StoreDestroyAPIView)


urlpatterns = [
    path('master/', include('masters.urls')),
    path('web/api/v1/all-web-houses', WebHomeListAPIView.as_view()),
    # path('web/api/v1/web-houses', WebHomeCreateView),
    # path('user/', include()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/categories/', CategoryListAPIView.as_view()),
    path('api/v1/houses/', HouseListAPIView.as_view()),
    # path('web/api/v1/web-houses/', WebHomeCreateView.as_view()),
    # path('api/v1/houses/create/', HouseAddCreateAPIView.as_view()),
    path('api/v1/houses/<int:pk>', HouseDetailAPIView.as_view()),
    path('api/v1/amenities/', AmenitiesListAPIView.as_view()),
    path('web/api/v1/web-amenities/', WebAmenitiesListAPIView.as_view()),
    path('web/api/v1/web-prices/', WebPriceListAPIView.as_view()),
    path('api/v1/maklers/', MasterListAPIView.as_view()),
    path('api/v1/maklers/<int:pk>', MasterDetailAPIView.as_view()),
    path('api/v1/store/', StoreModelAPIView.as_view()),
    path('api/v1/store/<int:pk>', StoreDetailAPIView.as_view()),
    # path('api/v1/store/create/', StoreAddCreateAPIView.as_view()),
    path('api/v1/fav/', HouseFavListAPIView.as_view()),
    path('api/v1/houses/image/', HouseImageAPIView.as_view()),
    path('api/v1/houses/archived/', HouseArchiveListAPIView.as_view()),
    # path('api/v1/login', LoginView.as_view()),
    # path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/users/', include('user.urls')),
    path('api/v1/all-users/', UserList.as_view()),
    path('api/v1/all-users/<int:pk>/', UserDetail.as_view()),
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('web2/', snippet_list),
]

urlpatterns += doc_urls
urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
