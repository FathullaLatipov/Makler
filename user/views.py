from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from masters.models import MasterModel
from products.models import HouseModel
from store.models import StoreModel
from .models import CustomUser

from products.serializers import HomeSerializer
from masters.serializers import MasterSerializer
from store.serializers import StoreModelSerializer

from .serializers import RegistrationSerializer, MyTokenObtainPairSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    ''' Регистрация юзера '''
    queryset = CustomUser.objects.all()
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


class UserProfile(APIView):
    get_serializer_class = None

    def get_object(self, user, pk=None):
        houses = HouseModel.objects.filter(creator=user)
        masters = MasterModel.objects.filter(creator=user)
        stores = StoreModel.objects.filter(creator=user)

        data = {
            'houses': houses,
            'masters': masters,
            'stores': stores
        }
        return data

    def get(self, request, **kwargs):
        announcements = self.get_object(user=request.user)
        housesserializer = HomeSerializer(announcements.get('houses'), many=True).data()
        mastersserializer = MasterSerializer(announcements.get('masters'), many=True).data()
        storesserializer = StoreModelSerializer(announcements.get('stores'), many=True).data()

        data = {
            'announcements': [housesserializer, mastersserializer, storesserializer]
        }
        return Response(data, status=200)
    # shu data ni olib bita view qb ushani ichiga chqarb qoysechi hamma danniy la shunda kevoriyu data da TG go tg ga

    #ishlatib korishimiz kere hurol yozing brnnasalar qling masalan??


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
