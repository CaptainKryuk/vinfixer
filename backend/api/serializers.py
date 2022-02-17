from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from users.models import User
from django.contrib.auth.hashers import make_password


class NewUserSerializer(Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()
    repeat_password = serializers.CharField()

    def create(self, validated_data):
        if validated_data.get('password') != validated_data.get('repeat_password'):
            return serializers.ValidationError("Passwords doesn't equal")

        user = User.objects.create(username=validated_data.get('username'),
                                   email=validated_data.get('email'),
                                   password=make_password(validated_data.get('password')))
        return user


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'