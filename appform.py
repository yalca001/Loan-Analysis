from flask import Flask, render_template, request, redirect, url_for
# rom werkzeug import secure_filename, FileStorage
import os
import pickle
import numpy as np
import pandas
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # gender = request.form['gender']
        # education = request.form['education']
        # married = request.form['married']
        # employment = request.form['employment']
        # property_location = request.form['property-location']
        income = request.form['income']
        coincome = request.form['coincome']
        credit = request.form['credit']
        loan_term = request.form['loan-term']
        user_data = [income, coincome, credit, loan_term]
        user_data = np.array(user_data).reshape(-1, 1)
        # put user data in a format to apply the scaler . reshape -1. -1 two dimension
        # after reshape load scaler and transform user data
        # load model and predict on scaled data
        # render from
        scaler = pickle.load(open("scaler_rfloans.sav", 'rb'))
        df_scaler = scaler.transform(df)
        df_scaler = df_scaler[["Credit_History", "ApplicantIncome",
                               "Loan_Amount_Term", "CoapplicantIncome"]]
        scaler = pickle.load(open("scaler_rfloans.sav", 'rb'))
        # load your model and scaler
        scaler = joblib.load("scalingfunction.sav")
        user_scaled = scaler.transform(user_data)
        user_prediction = model.predict(user_scaled)
        if int(prediction) == 0:
            prediction = message = "You did not get the loan!"
            image = "https://image.shutterstock.com/image-illustration/red-seal-imprint-loan-denied-260nw-311583383.jpg"
        else:
            message = "Huzzah! you got the loan"
            image = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSkG249Z0__YtoOsxIXUnRe_dRgpLo_oz3oxg&usqp"
            prediction_dict = {"message": message, "image": image}
    # user_data = request.form['user_data']
    # print(user_data)
        return render_template('form.html', result=result)
           else:
        return render_template('form.html')
# def runmodel(input_data):
#     input_data = preprocess(input_data)
#     rf_model = pickle.load(open('finalized_rfloans.sav', 'rb'))
#     y_predict = rf_model.predict(input_data)
#     return y_predict
#
# @app.route('/prediction', methods=['GET', 'POST'])
# def prediction():
#     user_input = request.form.to_dict()
#     user_input = list(user_input.values())
#     user_input = list(map(int, user_input))
#     prediction = runmodel(user_data)
#    # user prediction is going to be a 0 or a 1
#     if int(prediction) == 0:
#         prediction = message = "You did not get the loan!"
#         image = "https://image.shutterstock.com/image-illustration/red-seal-imprint-loan-denied-260nw-311583383.jpg"
#     else:
#         message = "Huzzah! you got the loan"
#         image = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSkG249Z0__YtoOsxIXUnRe_dRgpLo_oz3oxg&usqp"
#     prediction_dict = {"message": message, "image": image}
#     # load your model and scaler
#     scaler = joblib.load("scalingfunction.sav")
#     user_scaled = scaler.transform(user_data)
#     user_prediction = model.predict(user_scaled)
#     # returns the whole prediction string value when user submits the form
#     return render_template('results.html', prediction = prediction_dict)
#
if __name__ == "__main__":
    app.run(debug=True)
(20 kB)
https://image.shutterstock.com/image-illustration/red-seal-imprint-loan-denied-260nw-311583383.jpg
(10 kB)
https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSkG249Z0__YtoOsxIXUnRe_dRgpLo_oz3oxg&usqp

