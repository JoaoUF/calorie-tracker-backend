from rest_framework import serializers
from apps.myapp.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, data):
        user = CustomUser.objects._create_user(
            data['email'],
            data['password'],
        )
        user.save()
        return user
