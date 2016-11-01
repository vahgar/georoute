from rest_framework import serializers

from accounts.models import CustomUser


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['email','first_name','last_name','password']
        extra_kwargs = {"password" : {"write_only": True}}

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        CustomUser_object = CustomUser(email=email)
        CustomUser_object.set_password(password)
        CustomUser_object.save()
        return validated_data
