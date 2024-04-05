from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from apps.myapp.models import Consume
from apps.myapp.serializers import ConsumeSerializer


class ConsumeList(generics.ListCreateAPIView):
    queryset = Consume.objects.all()
    serializer_class = ConsumeSerializer
    permission_classes = [IsAuthenticated]


class ConsumeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consume.objects.all()
    serializer_class = ConsumeSerializer
    permission_classes = [IsAuthenticated]
