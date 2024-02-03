# Emotion Detection Web Application

## Introduction

This project is an Emotion Detection Web Application that utilizes the Watson NLP Library for sentiment analysis. The application is built using Flask for the server and includes a simple front-end interface for user interaction.

## Features

- **Emotion Detection**: Analyzes text input and determines the dominant emotion (anger, disgust, fear, joy, sadness).
- **Web Interface**: User-friendly web interface for entering text and viewing emotion analysis results.

## Project Structure

- **final_project/**: Main project folder.
  - **EmotionDetection/**: Python package containing the emotion detection functionality.
    - `__init__.py`: Package initialization file.
    - `emotion_detector.py`: Module containing the Emotion Detector function.
  - **static/**: Folder for static files.
    - `mywebscript.js`: JavaScript file for handling user interface interactions.
  - **templates/**: HTML templates for the web interface.
    - `index.html`: Main HTML file for the web interface.
  - `test_emotion_detection.py`: Unit tests for the emotion detection function.
  - `server.py`: Flask server script.
  - `README.md`: Project documentation.

## Installation and Usage

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd final_project
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask server:**

    ```bash
    python3.11 server.py
    ```

    The server will run at `http://127.0.0.1:5000/`.

4. **Access the application in your web browser:** `http://127.0.0.1:5000/`

## Usage Instructions

1. Enter the text to be analyzed in the provided input field.
2. Click the "Run Sentiment Analysis" button to submit the text.
3. View the results, including emotion scores and the dominant emotion.

## Unit Testing

To run unit tests, use the following command:

```bash
python3.11 -m unittest test_emotion_detection.py

