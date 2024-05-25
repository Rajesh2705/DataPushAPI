from rest_framework import serializers
from users.models import CustomUser
from destination.models import Destination, Header

from uuid import uuid4


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'name', 'website', 'token', 'password')
        read_only_fields = ('id', 'token')

    
class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ['id', 'key', 'value']

class DestinationSerializer(serializers.ModelSerializer):
    headers = HeaderSerializer(many=True)

    class Meta:
        model = Destination
        fields = ['url', 'http_method', 'headers']

    def create(self, validated_data):
        headers_data = validated_data.pop('headers', [])
        destination = Destination.objects.create(**validated_data, user=self.context['request'].user)

        for header_data in headers_data:
            Header.objects.create(destination=destination, **header_data)

        return destination
    
class IncomingDataSerializer(serializers.Serializer):
    data = serializers.JSONField()

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'website',  'password']

    def create(self, validated_data):
        token = str(uuid4())
        instance = self.Meta.model(token = token,**validated_data)
        instance.set_password(validated_data["password"])
        instance.save()
        return instance