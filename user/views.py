from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import CustomUser
from .serializers import RegistrationSerializer


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

