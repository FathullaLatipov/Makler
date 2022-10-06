from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .serializers import RegistrationSerializer, MyTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    ''' Регистрация юзера '''
    queryset = CustomUser.objects.all()
    ordering = ['-date_joined']
    search_fields = ['username']
    serializer_class = RegistrationSerializer

    def create(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True})
        else:
            return Response(serializer.errors)


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
