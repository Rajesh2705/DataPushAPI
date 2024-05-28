from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from users.models import CustomUser
from destination.models import Destination, Header
from .serializers import UserSerializer, DestinationSerializer, HeaderSerializer
from .serializers import UserLoginSerializer, UserRegistrationSerializer

class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)

    def update(self, request, *args, **kwargs):
        if request.user.id != kwargs['pk']:
            return Response(status=403)
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        if request.user.id != kwargs['pk']:
            return Response(status=403)
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    def get_permissions(self):
        if self.action in ['create_user', 'login', 'register']:
            return [AllowAny()]
        if self.action in ['logout']:
            return [IsAuthenticated()]
        if self.action in ['update', 'partial_update']:
            return [IsAuthenticated()]
        if self.action in ['destroy']:
            return [IsAdminUser()] 
        return super().get_permissions()

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'login_token': token.key, 'user_data': UserSerializer(user).data}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_data': UserSerializer(user).data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Destination.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers_data = request.data.get('headers', [])
        destination = serializer.save()

        for header_dict in headers_data:
            key = header_dict.get('key')
            value = header_dict.get('value')
            Header.objects.create(destination=destination, key=key, value=value)

        headers = destination.headers.values('key', 'value')
        return Response({'destination': serializer.data, 'headers': headers}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        headers = instance.headers.values('key', 'value')
        return Response({'destination': serializer.data, 'headers': headers})

class HeaderViewSet(viewsets.ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Header.objects.filter(destination__user=self.request.user)

    def perform_create(self, serializer):
        destination_id = self.request.data.get('destination')
        destination = get_object_or_404(Destination, id=destination_id, user=self.request.user)
        serializer.save(destination=destination)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers_data = request.data.get('headers', [])
        try:
            destination = get_object_or_404(Destination, id=request.data.get('destination'), user=self.request.user)
            for header_dict in headers_data:
                key = header_dict.get('key')
                value = header_dict.get('value')
                Header.objects.create(destination=destination, key=key, value=value)
            headers = destination.headers.values('key', 'value')
            return Response(headers, status=status.HTTP_201_CREATED)
        except NotFound:
            return Response({'error': 'Destination not found.'}, status=status.HTTP_404_NOT_FOUND)