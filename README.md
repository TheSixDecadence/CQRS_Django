# Django CQRS - Course System
This project implements the CQRS (Command Query Responsibility Segregation) architecture in Django for course management. It separates write (Commands) and read (Queries) operations into independent modules.

# Project Body
courses/

│─── models.py # CQRS models (CourseCommand and CourseQuery).

│─── commands.py # Logic for creating, updating and deleting courses.

│─── queries.py # Logic for querying courses.

│─── views.py # Class-based views to handle APIs.

│─── urls.py # Definition of routes for API.

elearning/

│─── settings.py # It's where the configuration of the project are

│─── urls.py # It's where the global URLs are

# How to install the project
As a reminder, you need to have installed Python and PIP, if you don't have any of those installed, here are the links:

Python:

https://www.geeksforgeeks.org/how-to-install-python-on-windows/

PIP:

https://www.geeksforgeeks.org/how-to-install-pip-on-windows/

1. You need to clone this repository
2. Once in the project folder, open your CMD and run this command: pip install -r requirements.txt
3. Configurate the database: python manage.py migrate
4. And finally run the server: python manage.py runserver
5. You have now access :)

# EndPoints
GET:

courses/

courses/:id:/


POST:

create/


PUT: 

update/:id:/


DELETE:

delete/:id:/

# Body for the EndPoints:
    {
      "title": "name of the course",
      "description": "description of the course"
    }

# Made By
- Daniel Enrique Alvarado Elias
- Sergio Iván Carreón Peña
- Jesús Alberto De los Santos Hernández
- Maria Janet Sanchéz Marta
- Brian Armando Sifuentes Muñoz

    - TIDBIS71N
