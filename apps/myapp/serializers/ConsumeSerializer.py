from rest_framework import serializers
from apps.myapp.models import Consume


class ConsumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consume
        fields = '__all__'
