from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_staff"
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "password_confirm",
            "first_name",
            "last_name"
        ]

    def validate(self, data):
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError(
                {"password_confirm": "Passwords do not match."}
            )

        validate_password(data["password"])

        return data

    def create(self, validated_data):
        validated_data.pop("password_confirm")

        password = validated_data.pop("password")

        user = User.objects.create(**validated_data)

        user.set_password(password)

        user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(
        source="user.first_name"
    )

    last_name = serializers.CharField(
        source="user.last_name"
    )

    email = serializers.EmailField(
        source="user.email",
        read_only=True
    )

    is_staff = serializers.BooleanField(
        source="user.is_staff",
        read_only=True
    )

    class Meta:
        model = UserProfile
        fields = [
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "phone",
            "date_of_birth",
            "profile_image"
        ]
