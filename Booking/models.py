from django.db import models

# Create your models here.

class FitnessClass(models.Model):
	'''
	A model for a class. 
	This model will have the information of a specific class with the name of the instructor and the number of slots
	'''
	CLASS_TYPES = [
			('Yoga', 'Yoga'),
			('Zumba', 'Zumba'),
			('HIIT', 'HIIT')
	]
	class_name = models.CharField(max_length=10, choices=CLASS_TYPES)
	instructor = models.CharField(max_length=120, null=False, blank=False)
	date = models.DateTimeField()
	total_slots = models.IntegerField()
	available_slots = models.IntegerField()

	def __str__(self):
		return (f"{self.class_name} class taken by {self.instructor}")


class Booking(models.Model):
	'''
	A model to manage the bookings.
	This model will have the details about the bookings that the customers have made.
	'''
	fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
	customer_name = models.CharField(max_length=120)
	customer_email = models.EmailField()

	def __str__(self):
		return (f"{self.customer_name} booked for a {self.class_name} class")

