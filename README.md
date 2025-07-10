# Tech Stack:
Python
Django Restframework

# Setup:
- Clone the repo using the below command
     git clone https://github.com/RamvilasRV/FitnessStudioBookingAPI.git
- Cd into the folder and install the dependencies using the below command
     pip install -r requirements.txt
- Run migrations
     python manage.py makemigrations
     python manage.py migrate
- (optional) Create a superuser
     python manage.py createsuperuser
- Run the server
     python manage.py runserver



# Sample API usages using CURL




Curl for testing

Get classes
curl -X GET http://127.0.0.1:8000/api/classes/

curl -X GET "http://127.0.0.1:8000/api/classes/?timezone=Europe/London"


book a class
curl -X POST http://127.0.0.1:8000/api/book/ ^
  -H "Content-Type: application/json" ^
  -d "{\"fitness_class\": 1, \"customer_name\": \"shiv\", \"customer_email\": \"shiv@test.com\"}"

curl -X POST http://127.0.0.1:8000/api/book/ ^
  -H "Content-Type: application/json" ^
  -d "{\"fitness_class\": 3, \"customer_name\": \"shiv\", \"customer_email\": \"shiv@test.com\"}"


Get the list of classes booked.
curl -X GET "http://127.0.0.1:8000/api/bookings/?email=shiv@test.com"

