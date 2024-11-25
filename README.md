# Portfolio Website - Rahul Gajjar

Welcome to my portfolio website project! This website showcases my educational background, professional experience, projects, and contact information, providing a professional digital presence to share with potential employers and collaborators.

## Features

- **Home Page:** Highlights the core purpose of the website.
- **Education:** Showcases my educational background, skills, and professional details.
- **Experience:** Details about my professional experience. 
- **Projects:** Lists key projects with descriptions and links to their repositories or live demos.
- **Contact Page:** A form for visitors to reach out to me.
- **Thank You Page:** A confirmation page displayed after a successful form submission.

## Tech Stack

- **Frontend:** HTML, CSS (with gradients and responsive design)
- **Backend:** Flask (Python)
- **Email Integration:** Flask-Mail for handling contact form submissions.
- **Deployment:** Can be hosted on platforms like Heroku, Vercel, or personal hosting services.

## Setup and Installation

Follow the steps below to set up and run the project locally:

1. Clone this repository:
    ```bash
    git clone repo-url
    cd folder-name
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the environment variables for email integration:
    Create a `.env` file in the root directory and add the following:
    ```env
    MAIL_USERNAME=your-email@gmail.com
    MAIL_PASSWORD=your-email-password
    ```

5. Run the Flask application:
    ```bash
    python app.py
    ```

6. Open your browser and visit:
    ```
    http://127.0.0.1:5000/
    ```

## Email Configuration

The contact form is configured using Flask-Mail. To enable it:
- Replace `MAIL_USERNAME` and `MAIL_PASSWORD` in the `.env` file with your email credentials.
- Ensure that "Less secure app access" is enabled for Gmail or use an app-specific password.