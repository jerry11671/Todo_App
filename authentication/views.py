from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            data['username'] = user.username
            data['email'] = user.email
            data['token'] = {
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }

            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user =authenticate(email=email, password=password)
        token = RefreshToken(user)

        return Response({'access_token': str(token.access_token)}, status=status.HTTP_202_ACCEPTED)
    

@api_view(['POST'])
def logout(request):
    if request.method == 'POST':
        try:
            refresh_token = request.data.get['access_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


