from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import CustomUser, Profile

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize CustomUser model.
    """

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email")

class UserRegisterationSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize registration requests and create a new user.
    """
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser

        # Removing the "username" field from this serializer did the trick:
        # Username field stopped showing up in the browsable API registration form
        fields = ("id", "email", "password", "password2")
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        attrs.pop('password2')
        return attrs
            
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer class to authenticate users with email and password.
    """

    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

class ProfileSerializer(CustomUserSerializer):
    """
    Serializer class to serialize the user Profile model
    """

    class Meta:
        model = Profile
        fields = ("bio",)

"""
# Disabling avatar capability for now
class ProfileAvatarSerializer(serializers.ModelSerializer):
    
    # Serializer class to serialize the avatar
    
    class Meta:
        model = Profile
        fields = ("avatar",)
"""