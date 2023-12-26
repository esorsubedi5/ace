from django.urls import reverse_lazy
from django.shortcuts import redirect
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .serializers import UserRegisterSerializer, UserLoginSerializer
from django.contrib.auth import get_user_model
from ace.views import home
User = get_user_model()

class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserLoginAPIView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])

        if user:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy(home))
