# 🏠 House Price Prediction using Linear Regression

## Project Description

This project is a Machine Learning web application that predicts house prices using the **Linear Regression** algorithm. Users can enter house details through a simple web interface, and the application estimates the house price based on a trained machine learning model.

The project is built using **Python, Flask, Scikit-Learn, HTML, and CSS**.


## Live Demo

🔗 **Live Application:**
https://house-price-prediction-778v.onrender.com


## Features

* Predict house prices using Machine Learning
* Linear Regression algorithm
* User-friendly web interface
* Responsive design
* Input validation
* Fast and accurate prediction
* Clean and modern UI

## Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Scikit-Learn
* Joblib
* HTML
* CSS


## Machine Learning Model

**Algorithm Used:** Linear Regression

The model is trained using the **Housing.csv** dataset to predict house prices based on different house features.


## Dataset

**Dataset Name:** Housing.csv

### Input Features

* Area
* Bedrooms
* Bathrooms
* Stories
* Main Road
* Guest Room
* Basement
* Hot Water Heating
* Air Conditioning
* Parking
* Preferred Area
* Furnishing Status

### Target Variable

* Price


## Model Evaluation

The model is evaluated using:

* Mean Squared Error (MSE)
* R² Score

## Project Structure

House_Price_Prediction/
│
├── app.py
├── train_model.py
├── house_price_model.pkl
├── Housing.csv
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
└── screenshots/
    ├── home.png
    └── prediction.png


## Installation

Install the required libraries:

pip install -r requirements.txt

Run the application:


python app.py


Open your browser and visit:

http://127.0.0.1:5000

## How to Use

1. Open the application.
2. Enter the house details.
3. Click **Predict House Price**.
4. View the predicted house price.

## Future Improvements

* Improve prediction accuracy
* Try advanced regression algorithms
* Add more property features
* Enhance the user interface

## Author

**Yogesh**

Machine Learning & Python Developer


