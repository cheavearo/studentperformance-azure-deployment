from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import os
import webbrowser 
from threading import Timer

from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application
## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods = ['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home_ui.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=request.form.get('reading_score'),
            writing_score=request.form.get('writing_score')
        )
        pred_df = data.get_data_as_datafram()

        print(pred_df)
        print("Before Prediction")
        
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(features=pred_df)
        print("After prediction of UI user dataframe")

        return render_template('home_ui.html', results = results[0])
def open_browser():
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new("http://127.0.0.1:5000/")
    
if __name__=="__main__":
    Timer(1, open_browser).start()
    app.run(host="0.0.0.0", debug=True)
    # Notes:
    # host: the hostname to listen on. Set this to '0.0.0.0' to have the server available externally as well. Defaults to '127.0.0.1' or the host in the SERVER_NAME config variable if present.
    # the port of the webserver. Defaults to 5000 or the port defined in the SERVER_NAME config variable if present.
    # So, the home page: http://127.0.0.1/5000
