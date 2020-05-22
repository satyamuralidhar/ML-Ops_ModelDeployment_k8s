from flask import Flask, request
import numpy as np
import pickle
import math
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

with open('model.pkl', 'rb') as model_pkl:
    rf = pickle.load(model_pkl)

 
@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["GET"])
def predict_note_authentication():
    
    """Let's Authenticate the Diabetis
    This is using docstrings for specifications.
    ---
    parameters:
        - name: Pregnancies
          in: query
          type: number
          required: true
        - name: Glucose
          in: query
          type: number
          required: true
        - name: BloodPressure	
          in: query
          type: number
          required: true
        - name: SkinThickness
          in: query
          type: number
          required: true
        - name: Insulin
          in: query
          type: number
          required: true
        - name: BMI
          in: query
          type: number
          required: true
        - name: DiabetesPedigreeFunction	
          in: query
          type: number
          required: true
        - name: Age	
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values
        
    """
    Pregnancies = request.args.get('Pregnancies')
    Glucose = request.args.get('Glucose')
    BloodPressure = request.args.get('BloodPressure')
    SkinThickness = request.args.get('SkinThickness')
    Insulin = request.args.get('Insulin')
    BMI = request.args.get('BMI')
    DiabetesPedigreeFunction = request.args.get('DiabetesPedigreeFunction')
    Age = request.args.get('Age')
    pred = np.array([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]).astype(np.float64)
    prediction = rf.predict(pred)
    print(prediction)
    return "result "+str(prediction)
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
    
