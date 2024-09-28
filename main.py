from fastapi import FastAPI

app = FastAPI()
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

@app.get("/")
def read_root():
    return {"Predicción de churn": "API para predecir si un cliente se va a ir o no"}

@app.post("/predict")
def predict(qorders: int,
 days_since_registration: int,
 days_since_last_purchase: int,
 qcity: int,
 app_type_COURIER: int,
 app_type_IPHONE: int,
 app_type_WEB: int,
 app_type_WEB_MOBILE: int,
 gender_MALE: int,
 gender_UNKNOWN: int,
 income_LOW: int,
 income_MID: int,
 income_MID_HIGH: int,
 income_MID_LOW: int,
 income_UNKNOWN: int,
 lifecycle_New: int,
 lifecycle_Onboarded: int,
 lifecycle_Prospect: int,
 lifecycle_Stable: int,
 lifecycle_Super_Heavy: int):
    features = [qorders,days_since_registration,days_since_last_purchase,qcity,app_type_COURIER,app_type_IPHONE,app_type_WEB,app_type_WEB_MOBILE,gender_MALE,gender_UNKNOWN,income_LOW,income_MID,income_MID_HIGH,income_MID_LOW,income_UNKNOWN,lifecycle_New,lifecycle_Onboarded,lifecycle_Prospect,lifecycle_Stable,lifecycle_Super_Heavy]
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": prediction.tolist()}
