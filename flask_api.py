# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:36:02 2022

@author: hp
"""

from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
    """Let's Authenticate the iris 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: SepalLengthCm
        in: query
        type: number
        required: true
      - name: SepalWidthCm
        in: query
        type: number
        required: true
      - name: PetalLengthCm
        in: query
        type: number
        required: true
         - name: PetalWidthCm
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    SepalLengthCm=request.args.get("SepalLengthCm")
    SepalWidthCm=request.args.get("SepalWidthCm")
    PetalLengthCm=request.args.get("PetalLengthCm")
    PetalWidthCm=request.args.get("PetalWidthCm")
     prediction=classifier.predict([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]]
    print(prediction)
    return "Hello The answer is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Let's Authenticate iris
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
    