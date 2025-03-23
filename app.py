from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from datetime import datetime, timedelta
import random
import string
import razorpay


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Gmail SMTP server
app.config['MAIL_PORT'] = 587                 # Port for sending emails
app.config['MAIL_USE_TLS'] = True             # Use TLS encryption
app.config['MAIL_USERNAME'] = 'vardhanchippada04@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'jgrs eary yowy hapc'     
app.config['MAIL_DEFAULT_SENDER'] = 'vardhanchippada04@gmail.com'  

razorpay_client = razorpay.Client(auth=("YOUR_KEY_ID", "YOUR_KEY_SECRET"))

mail = Mail(app)
# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False) 
    specialization = db.Column(db.String(100), nullable=True)  # ✅ New field (only for doctors)


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    patient_email = db.Column(db.String(100), nullable=False)  # Ensure this exists
    doctor_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), default="Pending")
    consultation_type = db.Column(db.String(20), nullable=False)  # 🛠 Add this column
    meet_link = db.Column(db.String(200))  # For online consultations





# Initialize Database
with app.app_context():
    db.create_all()

# Home Page
@app.route('/')
def home():
    if 'user' in session:
        role = session['role']
        username = session['user']

        if role == "patient":
            appointments = Appointment.query.filter_by(patient_name=username).all()
        elif role == "doctor":
            appointments = Appointment.query.filter_by(doctor_name=username).all()
        else:
            appointments = Appointment.query.all()  # For admins (if needed)

        return render_template('index.html', appointments=appointments, role=role)

    return redirect(url_for('login'))

@app.route('/payment', methods=['POST'])
def payment():
    amount = 50000  # ₹500 in paise
    order = razorpay_client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1"
    })
    return order

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        role = request.form['role']
        specialization = request.form['specialization'] if role == "doctor" else None  # ✅ Save only if doctor

        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))

        new_user = User(username=username, password=password, role=role, specialization=specialization)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/doctor_dashboard')
def doctor_dashboard():
    if 'user' not in session or session['role'] != 'doctor':
        flash('Access denied. Only doctors can view this page.', 'danger')
        return redirect(url_for('login'))

    doctor_name = session['user']
    appointments = Appointment.query.filter_by(doctor_name=doctor_name).all()

    return render_template('doctor_dashboard.html', appointments=appointments)


def generate_meet_link():
    """Generate a simple Google Meet-style link."""
    code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"https://meet.google.com/{code}"

@app.route('/approve_appointment/<int:id>')
def approve_appointment(id):
    if 'user' not in session or session['role'] != 'doctor':
        flash('Access denied.', 'danger')
        return redirect(url_for('login'))

    appointment = Appointment.query.get(id)
    if appointment:
        appointment.status = "Approved"

        if appointment.consultation_type == "Online":
            appointment.meet_link = generate_meet_link()  # Only for online consultations
            subject = "Your Online Consultation is Approved! ✅"
            body = f"Dear {appointment.patient_name},\n\nYour online appointment with Dr. {appointment.doctor_name} has been approved.\n\nJoin your consultation here: {appointment.meet_link}\n\nThank you!"
        else:
            subject = "Your In-Person Appointment is Approved! ✅"
            body = f"Dear {appointment.patient_name},\n\nYour in-person appointment with Dr. {appointment.doctor_name} is confirmed. Please visit the clinic on {appointment.date} at {appointment.time}.\n\nThank you!"

        db.session.commit()

        # Send email confirmation
        msg = Message(subject, recipients=[appointment.patient_email])
        msg.body = body
        mail.send(msg)

        flash('Appointment approved and email sent!', 'success')

    return redirect(url_for('doctor_dashboard'))


@app.route('/reject_appointment/<int:id>')
def reject_appointment(id):
    if 'user' not in session or session['role'] != 'doctor':
        flash('Access denied.', 'danger')
        return redirect(url_for('login'))

    appointment = Appointment.query.get(id)
    if appointment:
        appointment.status = "Rejected"
        db.session.commit()

        # ✅ Send rejection email
        subject = "Your Appointment has been Rejected ❌"
        body = f"Dear {appointment.patient_name},\n\nUnfortunately, your appointment with Dr. {appointment.doctor_name} on {appointment.date} at {appointment.time} has been rejected.\n\nPlease try booking another time.\n\nThank you!"

        msg = Message(subject, recipients=[appointment.patient_email])
        msg.body = body
        mail.send(msg)

        flash('Appointment rejected and email sent!', 'danger')

    return redirect(url_for('doctor_dashboard'))





# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user'] = user.username
            session['role'] = user.role
            return redirect(url_for('home'))

        flash('Invalid credentials', 'danger')
        return redirect(url_for('login'))

    return render_template('login.html')

# Book Appointment (Only Patients Can Book)
@app.route('/book', methods=['GET', 'POST'])
def book_appointment():
    if 'user' not in session:
        flash('You must be logged in to book an appointment.', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        email = request.form['email']
        doctor_name = request.form['doctor_name']
        date = request.form['date']
        time = request.form['time']
        consultation_type = request.form['consultation_type']

        new_appointment = Appointment(
            patient_name=session['user'],
            patient_email=email,
            doctor_name=doctor_name,
            date=date,
            time=time,
            status="Pending",
            consultation_type=consultation_type
        )
        db.session.add(new_appointment)
        db.session.commit()

        flash('Appointment booked successfully! Waiting for doctor approval.', 'success')
        return redirect(url_for('home'))

    doctors = User.query.filter_by(role='doctor').all()
    return render_template('book.html', doctors=doctors)






# Cancel Appointment
@app.route('/cancel/<int:id>')
def cancel(id):
    if 'user' not in session:
        flash('You must be logged in to cancel an appointment.', 'danger')
        return redirect(url_for('login'))

    appointment = Appointment.query.get(id)

    if not appointment:
        flash('Appointment not found!', 'danger')
        return redirect(url_for('home'))

    if session['role'] == 'patient' and appointment.patient_name != session['user']:
        flash('You can only cancel your own appointments!', 'danger')
        return redirect(url_for('home'))

    if session['role'] == 'doctor' and appointment.doctor_name != session['user']:
        flash('You can only cancel your own appointments!', 'danger')
        return redirect(url_for('home'))

    db.session.delete(appointment)
    db.session.commit()
    flash('Appointment canceled successfully!', 'success')
    
    return redirect(url_for('home'))

# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('role', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
