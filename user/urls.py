from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import UserProfile, UserList, UserDetail

# router = DefaultRouter()
# router.register('api/v1/signup', UserViewSet, 'signup')

urlpatterns = [
        # path('api/v1/users/', include('user.urls')),
        path('api/v1/all-users/', UserList.as_view()),
        path('api/v1/all-users/<int:pk>/', UserDetail.as_view()),
        path('profile/', UserProfile.as_view(), name='user-profile'),
]
