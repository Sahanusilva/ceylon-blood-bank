from rest_framework import viewsets
from . import models
from . import serializers

class Blood_donorViewset(viewsets.ModelViewSet):
    queryset = models.Blood_donor.objects.all()
    serializer_class = serializers.Blood_donorSerializer

class Blood_recipientViewset(viewsets.ModelViewSet):
    queryset = models.Blood_recipient.objects.all()
    serializer_class = serializers.Blood_recipientSerializer

class EventViewset(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

class MessageViewset(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer

class CityViewset(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer