from flask import Flask, render_template, request
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)

# Define a route for the contact form submission
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        # Capture form data
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Compose the email
        msg = Message(
            subject=f"Contact Form Submission: {subject}",
            sender=email,
            recipients=[os.getenv('MAIL_USERNAME')],  # Replace with your email
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )

        # Send the email
        mail.send(msg)

        # Redirect to a thank-you page
        return render_template('thank_you.html')

# Define routes for different pages
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)