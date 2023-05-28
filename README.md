"# hospital_management_system" 
# Installation and Setup

1. Clone the repository to your local machine:
$ git clone https://github.com/your-username/hospital-covid19-management.git

2. Change into the project directory:
$ cd hospital-covid19-management

3. Install the required dependencies:
$ pip install -r requirements.txt

4. Apply the database migrations:
$ python manage.py migrate

5. Create a superuser for accessing the Django admin panel:
$ python manage.py createsuperuser

6. Start the development server:
$ python manage.py runserver

7. Access the API in your browser at http://localhost:8000/