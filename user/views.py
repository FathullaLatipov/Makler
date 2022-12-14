from django.contrib.auth import logout
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics, permissions, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from masters.models import MasterModel
from products.models import HouseModel
from store.models import StoreModel
from .models import CustomUser

from products.serializers import HomeSerializer
from masters.serializers import MasterSerializer
from store.serializers import StoreModelSerializer

from .serializers import RegistrationSerializer, UserSerializer, LoginSerializer, UserALLSerializer, \
    UpdateUserSerializer, UserProductsSerializer


class UserViewSet(GenericViewSet):
    ''' Регистрация юзера '''
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer

    # @action(['POST'], detail=False, permission_classes=[permissions.AllowAny])
    def create(self, request: Request):
        self.serializer_class = RegistrationSerializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']
        token, created = CustomUser.objects.get_or_create(phone_number=phone_number)
        return Response({'token': token.tokens()})

    #
    # @action(['DELETE'], detail=False, permission_classes=[IsAuthenticated])
    # def logout(self, request: Request):
    #     Token.objects.get(user=request.user).delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# class LoginView(TokenObtainPairView):
# permission_classes = (AllowAny,)
# serializer_class = MyTokenObtainPairSerializer
# from django.contrib.auth import login, authenticate
#
#
# class LoginView(APIView):
#     def post(self, request):
#         phone_number = request.data['phone_number']
#         password = request.data['password']
#         user = authenticate(phone=phone_number, password=password)
#         if not user:
#             login(request, user)


class LoginView(GenericViewSet):
    serializer_class = LoginSerializer
    queryset = CustomUser.objects.all()

    @action(['POST'], detail=False, permission_classes=[permissions.AllowAny])
    def login(self, request: Request):
        self.serializer_class = LoginSerializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']
        code = serializer.validated_data['code']
        if int(code) == int(CustomUser.objects.get(phone_number=phone_number).mycode):

            token, created = CustomUser.objects.get_or_create(phone_number=phone_number)
            return Response({'token': token.tokens()})
        else:
            return Response({'error':f"Code is not valid! {code}=!{CustomUser.objects.get(phone_number=phone_number).mycode}"})

    @action(['POST'], detail=False, permission_classes=[permissions.IsAuthenticated])
    def logout(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        if not token.blacklist():
            return Response("Ошибка")
        else:
            return Response({"status": "Успешно"})


class UserProfile(APIView):
    get_serializer_class = None

    def get_object(self, user, pk=None):
        houses = HouseModel.objects.filter(creator=user)
        masters = MasterModel.objects.filter(owner=user)
        stores = StoreModel.objects.filter(creator=user)

        data = {
            'houses': houses,
            'masters': masters,
            'stores': stores,
        }
        return data

    def get(self, request, **kwargs):
        announcements = self.get_object(user=request.user)
        housesserializer = HomeSerializer(announcements.get('houses'), many=True).data
        mastersserializer = MasterSerializer(announcements.get('masters'), many=True).data
        storesserializer = StoreModelSerializer(announcements.get('stores'), many=True).data

        data = {
            'announcements': {'HOUSEMODEL': housesserializer, 'MASTERMODEL': mastersserializer,
                              'STORAGEMODEL': storesserializer}
        }
        return Response(data, status=200)


class UserList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        users = CustomUser.objects.get(id=pk)
        serializer = UserSerializer(users, context={'request': request})
        return Response(serializer.data)


class UserProductsList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        users = CustomUser.objects.get(id=pk)
        serializer = UserProductsSerializer(users, context={'request': request})
        return Response(serializer.data)

class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_summary="Получения данных пользователья(ЛК)",
        operation_description="Метод получения данных пользователья. Помимо типа данных и токен авторизации, передаётся только ID пользователья.",
    )
    def get(self, request, pk):
        users = CustomUser.objects.get(id=pk)
        serializer = UserALLSerializer(users, context={'request': request})
        return Response(serializer.data)


class UpdateProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UpdateUserSerializer
