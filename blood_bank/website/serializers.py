from rest_framework import serializers
from .models import Blood_donor
from .models import Blood_recipient
from .models import Event
from .models import Message
from .models import City

class Blood_donorSerializer(serializers.ModelSerializer):
    class Meta:
        model =Blood_donor
        fields = '__all__'

class Blood_recipientSerializer(serializers.ModelSerializer):
    class Meta:
        model =Blood_recipient
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model =Event
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model =Message
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model =City
        fields = '__all__'