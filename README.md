# 🏠 House Price Prediction using Linear Regression

## Project Description

This project is a Machine Learning web application that predicts the price of a house using the **Linear Regression** algorithm. Users can enter house details through a web interface, and the application estimates the house price based on the trained model.

The project is developed using **Python, Flask, Scikit-Learn, HTML, and CSS**.

## Features

- Predict house prices using Machine Learning
- Linear Regression model
- User-friendly web interface
- Responsive design
- Input validation
- Fast prediction
- Simple and clean UI


## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- HTML
- CSS


## Machine Learning Model

**Algorithm Used:** Linear Regression

The model is trained using the Housing dataset and predicts house prices based on different house features.


## Dataset

Dataset Name: **Housing.csv**

### Input Features

- Area
- Bedrooms
- Bathrooms
- Stories
- Main Road
- Guest Room
- Basement
- Hot Water Heating
- Air Conditioning
- Parking
- Preferred Area
- Furnishing Status

### Target Variable

- Price


## Model Evaluation

The model performance is evaluated using:

- Mean Squared Error (MSE)
- R² Score


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

### Install the required libraries

pip install -r requirements.txt


### Run the application

python app.py
Then open your browser and visit:
text
http://127.0.0.1:5000

## How to Use:
1. Open the application.
2. Enter the house details.
3. Click **Predict House Price**.
4. View the predicted house price.


## Future Improvements

- Improve prediction accuracy
- Try other regression algorithms
- Deploy the application online

## Author
**Yogesh**

