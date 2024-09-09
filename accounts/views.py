from cProfile import Profile
from django.shortcuts import render
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class SignUpAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)


class ProFileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

