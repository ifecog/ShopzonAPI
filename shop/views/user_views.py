from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework import status, viewsets

from shop.serializers import UserSerializer, MyTokenObtainPairSerializer, UserSerializerWithToken

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminUser,
        AllowAny
    ]
    
    def get_permissions(self):
        if self.action == 'get_users':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = super().get_permissions()
        return [permission() for permission in permission_classes]
            
    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser])
    def get_users(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)
    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register_user(self, request):
        data = request.data
        
        try:
            user = User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['email'],
                email=data['email'],
                password=make_password(data['password'])
            )
            serializer = UserSerializerWithToken(user, many=False)

            return Response(serializer.data)
        
        except:
            message = {'detail': 'user with this email already exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
