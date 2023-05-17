from rest_framework import serializers
from .models import Booking,Menu

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','Title','Price','Inventory']

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'