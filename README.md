# Smart-Appointment-Scheduler-for-clinic

This project is a Flask-based appointment scheduling system designed for clinics and hospitals.
It helps patients easily schedule appointments with doctors based on their specialization and availability. Doctors can approve or reject appointments, manage their schedules, and provide online consultations via Google Meet.
To enhance the user experience, the system includes email notifications to inform patients about their appointment status and integrates a payment gateway for online consultations. If a patient selects online consultation, the system generates a Google Meet link, which is shared upon doctor approval. Additionally, the system supports AI-powered appointment prioritization, allowing urgent cases to be scheduled earlier based on symptom severity.
This project is ideal for clinics, hospitals, and telemedicine platforms, providing an efficient and organized approach to appointment scheduling, video consultations, and payment processing.

~Features:<br>
1)User Authentication (Patients & Doctors)<br>
2)Doctor Dashboard (Approve/Reject Appointments)<br>
3)Appointment Booking System (In-Person & Online)<br>
4)Google Meet Link Generation (For Online Consultations)<br>
5)Email Notifications (Appointment Confirmation)<br>
6)Payment Gateway Integration (For Online Consultations)<br>
7)Specialization-Based Doctor Selection<br>
8)Smart Appointment Suggestions (Suggest Next Available Slot)<br>
9)AI-Powered Appointment Prioritization (Based on Symptoms)<br>

~Technologies Used:<br>
Backend: Flask (Python)<br>
Database: SQLite (SQLAlchemy ORM)<br>
Frontend: HTML, CSS, Bootstrap<br>
Authentication: Flask-Login, Flask-WTF<br>
Email Integration: Flask-Mail (SMTP)<br>
Video Consultation: Google Meet Link Generation<br>
Payment Gateway: Razorpay (or PayPal)<br>
AI for Prioritization: Machine Learning Model (Optional)<br>

~Usage Guide:<br>
Patients:<br>
Register/Login<br>
Choose a doctor (based on specialization)<br>
Select In-Person or Online Consultation<br>
If Online, complete payment<br>
Receive confirmation via email<br>

Doctors:<br>
Login to the Doctor Dashboard<br>
View, Approve/Reject appointments<br>
If Online, system generates a Google Meet Link<br>
Patients get an email notification<br>


~Setup & Installation
Clone the Repository:
git clone https://github.com/yourusername/smart-appointment-scheduler.git  
cd smart-appointment-scheduler  

Install Dependencies:
pip install -r requirements.txt  

Initialize the Database:
from app import db, app
with app.app_context():
    db.create_all()
    print("Database updated successfully!")

Run the Flask App:
python app.py  

