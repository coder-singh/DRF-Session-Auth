
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import logout

from auth_api.serializers import RegistrationSerializer, LoginSerializer, AccountSerializer

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

@api_view(['POST',])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    print(request.data)
    data = {}
    if serializer.is_valid(raise_exception=True):
        account = serializer.save()
        data['message'] = "Successfully Registered"
        data['username'] = account.username
        data['name'] = account.name
        data['email'] = account.email
        data['phone'] = account.phone
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        data = serializer.errors
        return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.data
        print(data)
        return Response(data, status=status.HTTP_200_OK)
    else:
        data = serializer.errors
        print(data)
        return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    data = {'message' : 'Logged out successfully'}
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    account = request.user
    serializer = AccountSerializer(account)
    return Response(serializer.data, status=status.HTTP_200_OK)