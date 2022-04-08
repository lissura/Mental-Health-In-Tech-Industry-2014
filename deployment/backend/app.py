import pickle
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)
with open ("pipe.pkl",'rb') as f:
    model = pickle.load(f)


results = ['No Need Treatment', 'Need Treatment']
columns  =['gender', 'country','mental_health_consequence','anonymity',
           'leave','obs_consequence','benefits','care_options','family_history','work_interfere']

@app.route("/")
def my_profile():
    return "<h1> It Works! </h1>"


@app.route("/predict", methods=['GET','POST'])
def model_prediction():
    if request.method == "POST":
        content = request.json
        try :
            data = [content['gender'],
            content['continent'],
            content['mental_health_consequence'],
            content['anonymity'],
            content['leave'],
            content['obs_consequence'],
            content['benefits'],
            content['care_options'],
            content['family_history'],
            content['work_interfere']]
            data = pd.DataFrame([data], columns = columns)
            res = model.predict(data)
            response = {'code':200, 'status': 'Ok', 'result': {'description':results[res[0]]}}
            return jsonify(response)
        except Exception as e :
            response2 = {'code':500, 'status' : 'Error','result' : {'error_msg':str(e)}}
            return jsonify(response2) 
    return "<p> Please Use Post Methods To Access The Prediction </p>"