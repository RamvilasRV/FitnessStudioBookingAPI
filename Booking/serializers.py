from rest_framework import serializers
from .models import FitnessClass, Booking

class FitnessClassSerializer(serializers.ModelSerializer):
	class Meta:
		model = FitnessClass
		fields = '__all__'

class Booking(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = "__all__"