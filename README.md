Project Overview
The Document Tracking System is a web-based application built using Django that allows departments to manage and track the progress of various documents. This system provides a user-friendly interface for tracking document statuses, viewing details, and managing documents within an organization.

Features
User Authentication: Secure login functionality for users to access the system.
Department Dashboard: A department-specific dashboard that displays all documents related to that department along with their statuses.
Super Admin Dashboard: A dashboard for super admins to monitor and track the status of documents across all departments.
Document Tracking: Ability to track the progress and status of each document through the workflow.
Document Viewing: Access and view documents directly from the system.
Visual Status Representation: Pie charts to visually represent the status distribution of documents (e.g., Approved, Pending, Rejected, Transit).
Technologies Used
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript (Chart.js)
Database: MySQL
Version Control: Git
Installation
Prerequisites
Python 3.x
Django 4.x
MySQL
Setup
Clone the Repository

git clone https://github.com/yourusername/document-tracking-system.git
cd document-tracking-system
Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies

pip install -r requirements.txt
Set Up the Database

Ensure MySQL is installed and running.
Create a database named file_management.
Update the database credentials in the settings.py file under DATABASES.
Apply Migrations

python manage.py makemigrations
python manage.py migrate
Run the Development Server

python manage.py runserver
Access the Application

Open your web browser and go to http://127.0.0.1:8000/login/.
Project Structure
Login_Page: Handles user authentication and login.
Depart_Dashboard: Manages and displays the department-specific dashboard.
Super_Dashboard: Provides the super admin view for tracking documents across all departments.
Document_Details: Manages and displays document details and tracking information.
Usage
Login
Use your Officer ID and Password to log in.
Depending on the ID, you will be redirected to either the Department Dashboard or the Super Admin Dashboard.
Department Dashboard
View all documents related to your department.
Track the status and progress of each document.
Click on Track to view detailed tracking information for a document.
Click on View to access the document.
Super Admin Dashboard
Monitor document status across all departments.
Visualize document status distribution using the pie chart.
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch for your feature or bugfix.
git checkout -b feature-name
Commit your changes.
git commit -m "Description of your changes"
Push to your branch.
git push origin feature-name
Open a pull request.
