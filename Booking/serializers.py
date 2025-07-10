from rest_framework import serializers
from .models import FitnessClass, Booking

class FitnessClassSerializer(serializers.ModelSerializer):
	class Meta:
		model = FitnessClass
		fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
	fitness_class = serializers.PrimaryKeyRelatedField(queryset=FitnessClass.objects.all())

	class Meta:
		model = Booking
		fields = "__all__"
