
 File  Tracking System

 Project Overview
The Document Tracking System is a web-based application built with Django that allows departments to manage and track the progress of various documents. It provides a user-friendly interface for tracking document statuses, viewing details, and managing documents within an organization.

 Features
- User Authentication: Secure login for users.
- Department Dashboard: Displays all documents related to a department and their statuses.
- Super Admin Dashboard: Monitors and tracks documents across all departments.
- Document Tracking: Tracks the progress and status of each document.
- Document Viewing: Access and view documents directly from the system.
- Visual Status Representation: Pie charts to show the status distribution of documents (e.g., Approved, Pending, Rejected, Transit).

 Technologies Used
- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript (Chart.js)
- Database: MySQL
- Version Control: Git

 Installation

 Prerequisites
- Python 3.x
- Django 4.x
- MySQL

 Setup
1. Clone the Repository
   bash
   git clone https://github.com/yourusername/document-tracking-system.git
   cd document-tracking-system
   

2. Create and Activate a Virtual Environment
   bash
   python -m venv venv
   source venv/bin/activate   On Windows use venv\Scripts\activate
   

3. Install Dependencies
   bash
   pip install -r requirements.txt
   

4. Set Up the Database
   - Ensure MySQL is installed and running.
   - Create a database named file_management.
   - Update the database credentials in settings.py under DATABASES.

5. Apply Migrations
   bash
   python manage.py makemigrations
   python manage.py migrate
   

6. Run the Development Server
   bash
   python manage.py runserver
   

7. Access the Application
   Open your web browser and go to [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/).

 Project Structure
- Login_Page: Handles user authentication and login.
- Depart_Dashboard: Manages and displays the department-specific dashboard.
- Super_Dashboard: Provides the super admin view for tracking documents across all departments.
- Document_Details: Manages and displays document details and tracking information.

 Usage
- Login: Use your Officer ID and Password to log in. Depending on your ID, you will be redirected to either the Department Dashboard or the Super Admin Dashboard.
- Department Dashboard: View and track documents related to your department. Click on "Track" for detailed tracking information and "View" to access the document.
- Super Admin Dashboard: Monitor document statuses across all departments and visualize status distribution using the pie chart.

 Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
   bash
   git checkout -b feature-name
   
3. Commit your changes.
   bash
   git commit -m "Description of your changes"
   
4. Push to your branch.
   bash
   git push origin feature-name
   
5. Open a pull request.

---

Feel free to adjust any sections as needed!
