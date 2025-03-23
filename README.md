# Smart-Appointment-Scheduler-for-clinic

Smart Appointment Scheduler with Online Consultation & Payment Integration
This project is a Flask-based appointment scheduling system designed for clinics and hospitals. It allows patients to book appointments with doctors, supports online consultations via Google Meet, and integrates a payment gateway for virtual consultations.

Features:
1)User Authentication (Patients & Doctors)
2)Doctor Dashboard (Approve/Reject Appointments)
3)Appointment Booking System (In-Person & Online)
4)Google Meet Link Generation (For Online Consultations)
5)Email Notifications (Appointment Confirmation)
6)Payment Gateway Integration (For Online Consultations)
7)Specialization-Based Doctor Selection
8)Smart Appointment Suggestions (Suggest Next Available Slot)
9)AI-Powered Appointment Prioritization (Based on Symptoms)

Technologies Used
Backend: Flask (Python)
Database: SQLite (SQLAlchemy ORM)
Frontend: HTML, CSS, Bootstrap
Authentication: Flask-Login, Flask-WTF
Email Integration: Flask-Mail (SMTP)
Video Consultation: Google Meet Link Generation
Payment Gateway: Razorpay (or PayPal)
AI for Prioritization: Machine Learning Model (Optional)

Usage Guide
Patients:
Register/Login
Choose a doctor (based on specialization)
Select In-Person or Online Consultation
If Online, complete payment
Receive confirmation via email

Doctors:
Login to the Doctor Dashboard
View, Approve/Reject appointments
If Online, system generates a Google Meet Link
Patients get an email notification

