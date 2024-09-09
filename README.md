# MNIST App

This is a Flask-based web application that allows users to draw a number on a canvas and obtain a prediction from a trained neural network model. The model is pre-trained to recognize hand-drawn digits, and this application demonstrates the prediction capabilities.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [How to Use](#how-to-use)
- [File Structure](#file-structure)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)

## Project Overview
The application consists of a front-end interface where users can draw digits on a canvas. This image is then sent to a Flask back-end server, where it is processed and fed into a pre-trained deep learning model that predicts the digit. The back-end uses a Keras-based model trained on the MNIST dataset.

## Features
- User-friendly interface to draw digits on a canvas.
- Real-time digit prediction using a neural network.
- Responsive design using Bootstrap.
- Image processing and handling with OpenCV and Numpy.
- Model loading and prediction using Keras.

## Setup Instructions

### Prerequisites
- Python 3.x
- `pip` or `pipenv` for dependency management

### Clone the repository
```bash
git clone https://github.com/yourusername/flask-image-prediction.git
cd flask-image-prediction
```

### Install dependencies
Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate # For Windows: venv\Scripts\activate
```

Install the required dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Download the model
Place the `model.json` and `mnist_model.h5` files inside the `models/` directory. These files should contain your pre-trained model architecture and weights.

### Run the application
To run the Flask application, execute the following command:
```bash
python app.py
```

The application will be accessible at [http://localhost:8000](http://localhost:8000).

## How to Use
1. Open the application in your browser at `http://localhost:8000`.
2. Use the canvas provided to draw a digit (0-9).
3. Click the "Predict" button to submit the drawing.
4. The predicted digit will be displayed below the canvas.

## File Structure
```
├── app.py              # Main Flask application
├── models
│   ├── load.py         # Model loading script
│   ├── model.json      # Pre-trained model architecture
│   └── mnist_model.h5  # Pre-trained model weights
├── static
│   ├── style.css       # Custom styles
│   └── index.js        # Front-end JavaScript
├── templates
│   ├── index.html      # Main HTML page
│   └── draw.html       # Drawing page
├── README.md           # Project documentation
├── app.ipynb           # Models generation
└── requirements.txt    # Python dependencies
```

## Technologies Used
- **Flask**: A lightweight web framework for Python.
- **Keras**: For building and loading the neural network model.
- **OpenCV**: For image processing and resizing.
- **NumPy**: For array manipulations and data formatting.
- **HTML5 Canvas**: For the drawing interface.
- **Bootstrap**: For a responsive and mobile-friendly UI.

## Future Improvements
- **Add More Models**: Extend the application to support multiple models and prediction tasks (e.g., letters or symbols).
- **Enhance UI**: Provide more drawing tools, such as pen thickness, color selection, and an eraser.
- **Improve Error Handling**: Add user-friendly error messages and validation for better user experience.
- **Deploy on a Cloud Platform**: Deploy the application on a platform like Heroku or AWS for wider accessibility.
  
## License
This project is licensed under the MIT License.