from django.urls import path

from . import views

urlpatterns = [
    path('classes/', views.ClassListView.as_view(), name="classes"),
    path('book/', views.BookingView.as_view(), name="book"),
    path('bookings/', views.BookingListView.as_view(), name="bookings")
]