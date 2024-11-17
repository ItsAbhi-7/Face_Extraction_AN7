# Face Extraction Project
This repository contains a Python-based application for extracting faces from images using the RetinaFace library. The application is built with Streamlit for an intuitive and interactive user interface.

# Features
- Face Detection and Extraction: Automatically detects and extracts faces from uploaded images.
* Streamlit-based Web App: User-friendly interface to upload and view results directly in the browser.
- Robust Processing: Supports common image formats such as JPG, PNG, and JPEG.
* Dynamic Feedback: Displays the uploaded image and extracted faces in real-time.

# Requirements
Ensure you have the following Python libraries installed:

* **RetinaFace**: For face detection and extraction.
* **Streamlit**: To create the web interface.
* **Pillow**: For image processing.
* **NumPy**: For handling image data arrays.

You can install these dependencies using pip:

pip install retinaface streamlit pillow numpy

# How to Use
1. Clone the Repository:

git clone https://github.com/your_username/face-extraction.git
cd face-extraction

2. Run the Application:

streamlit run app.py

3. Upload an Image:

* Use the "Upload a photo" button to upload an image (JPG, PNG, or JPEG).
* The application will detect and display any faces found in the uploaded image.
  
4. View Results:

* If faces are detected, they will be displayed as individual images.
* If no faces are detected, a message will inform you.

