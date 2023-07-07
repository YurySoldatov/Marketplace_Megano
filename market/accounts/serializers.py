from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile, Avatar


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя"""

    class Meta:
        model = User
        fields = ['username', 'password']


class AvatarSerializer(serializers.ModelSerializer):
    """Сериализатор аватарки"""

    class Meta:
        model = Avatar
        fields = ['src', 'alt']


class ProfileSerializer(serializers.ModelSerializer):
    """Сериализатор профиля пользователя"""

    class Meta:
        model = Profile
        fields = '__all__'

    avatar = AvatarSerializer(many=False, required=False)


class PasswordChangeSerializer(serializers.Serializer):
    """Сериализатор смены пароля"""

    passwordCurrent = serializers.CharField(required=True)
    passwordReply = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
