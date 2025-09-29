# Create a backend for a  my portfolio website
# The backend will be a Flask application that will be used to serve the frontend
# The backend will be used to serve the frontend and the backend will be used to serve the backend

from flask import Flask, request, jsonify, send_from_directory  # This is the Flask library for the backend
from flask_cors import CORS # This is the CORS library for the backend
import os

# Create Flask app instances
app = Flask(__name__, static_folder='../frontend')

# ENABLE CORS FOR ALL ROUTES 
CORS(app)

# Define routes
@app.route("/")
def home():
    return send_from_directory('../frontend/html pages', 'Home.html')

@app.route("/about")
def about():
    return send_from_directory('../frontend/html pages', 'about.html')

@app.route("/technicalSkills")
def technicalSkills():
    return send_from_directory('../frontend/html pages', 'technicalSkills.html')

@app.route("/projects")
def projects():
    return send_from_directory('../frontend/html pages', 'Projects.html')

@app.route("/certifications")
def certifications():
    return send_from_directory('../frontend/html pages', 'Certifications.html')

@app.route("/education")
def education():
    return send_from_directory('../frontend/html pages', 'Education.html')

@app.route("/workExperience")
def work_experience():
    return send_from_directory('../frontend/html pages', 'WorkExperience.html')

# Serve static files (CSS, JS, images)
@app.route('/style/<path:filename>')
def serve_css(filename):
    return send_from_directory('../frontend/style', filename)

@app.route('/script/<path:filename>')
def serve_js(filename):
    return send_from_directory('../frontend/script', filename)









# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5003)
     

