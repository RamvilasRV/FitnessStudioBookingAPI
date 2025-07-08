from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer

class ClassListView(APIView):
	'''
	A view to list all the types of classes and the slots
	'''
	def get(self, request):
		classes = FitnessClass.objects.all()
		serializer_class = FitnessClassSerializer(classes, many=True)
		return Response(serializer_class.data)


class BookingView(APIView):
	'''
	A view for the customer to book a slot in their desired class
	'''
	def post(self, request):
		serializer_class = BookingSerializer(data=request.data)

		if not serializer.is_valid():
			return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			selected_class = serializers.validated_data["fitness_class"]

		if selected_class.available_slots<0:
			return Response({"error":"Slots are not available for this class"})
		else:
			serializer_class.save()
			selected_class.available_slots =-1
			fitness_class.save()

		return Response({"message":"Your seat has been booked"}, status=status.HTTP_201_CREATED)

class BookingListView(APIView):
	'''
	A view to get the list of all booking based on the email provided in query parameter.
	'''
	def get(self, request):
		email = request.query_params.get("email")

		if not email:
			return Response({"error":"Please provide your email"})
		else:
			bookings = Booking.objects.filter(customer_email)
			serializer_class = BookingSerializer(bookings, many=True)
			return Response(serializer_class.data)