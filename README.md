# Banking System

This is a simple Banking App with features to display customer details, transfer money from one customer to another and view transaction history.

Developed By : Madhumitha J R

Purpose : Web Development Internship Task under The Sparks Foundation

Technologies Used : Python + Django Framework, HTML, CSS, SQL Database

Contact : madhumithajr16@gmail.com

To run this project, download all the source code and follow these steps:
  1. Install Python on your system.
  2. Create a folder titled 'Django'.
  3. Open cmd prompt and create a virtual environment using the command: py -m venv <project-name>
  4. Activate the virtual environment: project-name\Scripts\activate.bat
  5. Install Django: py -m pip install Django
  6. Place the 'Banking' directory and the 'project-name' directory inside the 'Django' directory.
  7. Change directory: cd Banking
  8. Migrate the project: python manage.py makemigrations
                          python manage.py migrate
  9. To load sample data into the database from fixtures, use: python manage.py loaddata sampledata.json
  10. To run the server: python manage.py runserver
  11. Open your web browser and go to: localhost:8000/Banking/index
  
