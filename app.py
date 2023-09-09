from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact_form.db'
db = SQLAlchemy(app)

class ContactFormSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    subject = db.Column(db.String(200))
    message = db.Column(db.Text())


with app.app_context():
    db.create_all()

# Define a route for the contact form submission
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        # Capture form data
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        submission = ContactFormSubmission(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Add the submission to the database and commit the transaction
        db.session.add(submission)
        db.session.commit()

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



