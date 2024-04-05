from rest_framework import generics
from apps.myapp.models import Consume
from apps.myapp.serializers import ConsumeSerializer


class ConsumeList(generics.ListCreateAPIView):
    queryset = Consume.objects.all()
    serializer_class = ConsumeSerializer


class ConsumeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consume.objects.all()
    serializer_class = ConsumeSerializer
