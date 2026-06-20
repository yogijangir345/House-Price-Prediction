from flask import Flask, render_template, request
import joblib
import pandas as pd

# Create Flask App
app = Flask(__name__)

# Load Trained Model
model = joblib.load("house_price_model.pkl")


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get Form Data
        area = float(request.form["area"])
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])
        stories = int(request.form["stories"])
        mainroad = int(request.form["mainroad"])
        guestroom = int(request.form["guestroom"])
        basement = int(request.form["basement"])
        hotwaterheating = int(request.form["hotwaterheating"])
        airconditioning = int(request.form["airconditioning"])
        parking = int(request.form["parking"])
        prefarea = int(request.form["prefarea"])
        furnishingstatus = int(request.form["furnishingstatus"])

        # Create DataFrame (same format as training data)
        features = pd.DataFrame([{
            "area": area,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "stories": stories,
            "mainroad": mainroad,
            "guestroom": guestroom,
            "basement": basement,
            "hotwaterheating": hotwaterheating,
            "airconditioning": airconditioning,
            "parking": parking,
            "prefarea": prefarea,
            "furnishingstatus": furnishingstatus
        }])

        # Predict Price
        prediction = model.predict(features)[0]
        prediction = round(prediction)

        return render_template(
            "index.html",
            prediction_text=f"🏠 Estimated House Price: ₹ {prediction:,}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)