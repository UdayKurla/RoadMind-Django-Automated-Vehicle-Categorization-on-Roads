# RoadMind: Automated Vehicle Categorization System

RoadMind is a sophisticated traffic monitoring and analysis platform. It leverages **Django** for a robust web architecture and **YOLOv8** for state-of-the-art computer vision to detect, classify, and analyze traffic patterns from image data.

## Key Features
* **Intelligent Object Detection:** Utilizes YOLOv8 (You Only Look Once) to identify vehicles and pedestrians with high precision.
* **Automated Categorization:** Classifies detections into specific categories such as cars, trucks, buses, and pedestrians.
* **Traffic Density Estimation:** Automatically evaluates road conditions as "Dense" or "Less Dense" based on real-time object counts.
* **Visual Analytics:** Generates annotated images featuring bounding boxes and confidence scores for every detected object.

## Technology Stack
* **Backend Framework:** Django 6.0
* **Computer Vision:** Ultralytics YOLOv8
* **Image Processing:** OpenCV & NumPy
* **Frontend Styling:** Tailwind CSS
* **Icons:** Remix Icon

## Installation and Setup

Follow these steps to get the project running on your local machine:

### 1. Clone the Repository

git clone [https://github.com/YourUsername/RoadMind_Django.git](https://github.com/YourUsername/RoadMind_Django.git)
cd RoadMind_Django

### 2. Set Up a Virtual Environment

Create and activate a separate environment to manage dependencies:
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

### 3. Install Dependencies

Install the required libraries listed in the requirements file:
pip install -r requirements.txt

### 4. Database Migrations

Initialize the Django database schema:
python manage.py migrate

### 5. Run the Application

Launch the development server:
python manage.py runserver
Access the application at http://127.0.0.1:8000/.


### Project Structure
roadmind_project/: Project-level settings, middleware, and main URL configurations.

traffic_app/: Application logic including views, templates, static assets, and AI utility functions.

media/: Dedicated storage for user-uploaded images and AI-processed outputs.

static/: Assets such as team photos and local site maps.

The Development Team
Dr. Senthil Kumar T - Project Guide (Professor, School of Computing, Coimbatore)

Mr. Kurla Uday Kiran Reddy - Student, Amrita Vishwa Vidyapeetham

Mr. Harish C M - Student, Amrita Vishwa Vidyapeetham