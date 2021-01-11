from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from auth_api.serializers import RegistrationSerializer, LoginSerializer, AccountSerializer

from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

@api_view(['POST',])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    print(request.data)
    data = {}
    if serializer.is_valid(raise_exception=True):
        account = serializer.save()
        data['response'] = "Successfully Registered"
        data['username'] = account.username
        data['name'] = account.name
        data['email'] = account.email
        data['phone'] = account.phone
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
    else:
        data = serializer.errors
        print(data)
    return Response(data)