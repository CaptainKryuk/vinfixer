from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from users.models import User, UserEmail
from django.contrib.auth.hashers import make_password
from postmarker.core import PostmarkClient
from django.conf import settings
from users.models import UserEmail

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


class UserEmailSerializer(ModelSerializer):
    class Meta:
        model = UserEmail
        fields = '__all__'


class RequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    message = serializers.CharField()

    def create(self, validated_data):
        UserEmail.objects.create(email=validated_data['email'])
        try:
            postmark_client =PostmarkClient(server_token=settings.POSTMARK_API_KEY)
            postmark_client.emails.send(
                From=settings.POSTMARK_SENDER,
                To='bestrongwb@gmail.com',
                Subject='Message from user',
                HtmlBody=f'{validated_data["name"]} -- {validated_data["message"]}'
            )
        except:
            pass
        return '200'