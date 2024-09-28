from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get form data
    qorders = int(request.form["qorders"])
    days_since_registration = int(request.form["days_since_registration"])
    days_since_last_purchase = int(request.form["days_since_last_purchase"])
    qcity = int(request.form["qcity"])
    app_type_COURIER = int(request.form["app_type_COURIER"])
    app_type_IPHONE = int(request.form["app_type_IPHONE"])
    app_type_WEB = int(request.form["app_type_WEB"])
    app_type_WEB_MOBILE = int(request.form["app_type_WEB_MOBILE"])
    gender_MALE = int(request.form["gender_MALE"])
    gender_UNKNOWN = int(request.form["gender_UNKNOWN"])
    income_LOW = int(request.form["income_LOW"])
    income_MID = int(request.form["income_MID"])
    income_MID_HIGH = int(request.form["income_MID_HIGH"])
    income_MID_LOW = int(request.form["income_MID_LOW"])
    income_UNKNOWN = int(request.form["income_UNKNOWN"])
    lifecycle_New = int(request.form["lifecycle_New"])
    lifecycle_Onboarded = int(request.form["lifecycle_Onboarded"])
    lifecycle_Prospect = int(request.form["lifecycle_Prospect"])
    lifecycle_Stable = int(request.form["lifecycle_Stable"])
    lifecycle_Super_Heavy = int(request.form["lifecycle_Super_Heavy"])
    
    # Prepare features for prediction
    features = [
        qorders, days_since_registration, days_since_last_purchase, qcity,
        app_type_COURIER, app_type_IPHONE, app_type_WEB, app_type_WEB_MOBILE,
        gender_MALE, gender_UNKNOWN, income_LOW, income_MID, income_MID_HIGH,
        income_MID_LOW, income_UNKNOWN, lifecycle_New, lifecycle_Onboarded,
        lifecycle_Prospect, lifecycle_Stable, lifecycle_Super_Heavy
    ]
    
    features = np.array(features).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(features)
    
    # Return prediction result
    return render_template("result.html", prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)
