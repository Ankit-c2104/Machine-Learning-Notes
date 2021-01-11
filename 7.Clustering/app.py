# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle
from flask import Response
import numpy as np

app = Flask(__name__) # initializing a flask app


@app.route('/predict',methods=['POST','GET']) # route to show the predictions
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            annual_income=float(request.json['annual_income'])
            spending_score = float(request.json['spending_score'])
            filename = 'finalized_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict(np.asarray([[annual_income,spending_score]]))
            print('prediction is', (list(prediction)[0]))
            # showing the prediction results in a UI
            return Response(str((list(prediction)[0])))
        except Exception as e:
            print('The Exception message is: ',e)
            return Response('something is wrong.')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
   app.run(debug=True) # running the app
