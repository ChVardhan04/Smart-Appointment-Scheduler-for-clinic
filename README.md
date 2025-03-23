# Smart-Appointment-Scheduler-for-clinic

Smart Appointment Scheduler with Online Consultation & Payment Integration
This project is a Flask-based appointment scheduling system designed for clinics and hospitals. It allows patients to book appointments with doctors, supports online consultations via Google Meet, and integrates a payment gateway for virtual consultations.

Features:<br>
1)User Authentication (Patients & Doctors)<br>
2)Doctor Dashboard (Approve/Reject Appointments)<br>
3)Appointment Booking System (In-Person & Online)<br>
4)Google Meet Link Generation (For Online Consultations)<br>
5)Email Notifications (Appointment Confirmation)<br>
6)Payment Gateway Integration (For Online Consultations)<br>
7)Specialization-Based Doctor Selection<br>
8)Smart Appointment Suggestions (Suggest Next Available Slot)<br>
9)AI-Powered Appointment Prioritization (Based on Symptoms)<br>

Technologies Used:<br>
Backend: Flask (Python)<br>
Database: SQLite (SQLAlchemy ORM)<br>
Frontend: HTML, CSS, Bootstrap<br>
Authentication: Flask-Login, Flask-WTF<br>
Email Integration: Flask-Mail (SMTP)<br>
Video Consultation: Google Meet Link Generation<br>
Payment Gateway: Razorpay (or PayPal)<br>
AI for Prioritization: Machine Learning Model (Optional)<br>

Usage Guide:<br>
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

