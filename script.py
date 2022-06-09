#importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '!Hello Mundo!'

@app.route('/prediccion')
def predict():
    return 'Predicciòn'

if __name__== "__main__":
    app.run()
