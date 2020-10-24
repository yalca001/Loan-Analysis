from flask import Flask, render_template, request, redirect, url_for
import os
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        gender = request.form['gender']
        married = request.form['married']
        employment = request.form['employment']
        income = request.form['income']
        coincome = request.form['coincome']
        credit = request.form['credit']
        loan_term = request.form['loan-term']

        user_data = {
            "gender": gender,
            "married": married, 
            "employment": employment,
            "income": income, 
            "coincome": coincome, 
            "credit": credit, 
            "loan_term": loan_term,
        }
       
        user_df = pd.DataFrame(data = user_data, index=[1])
        print(user_df)
        
        scaler = pickle.load(open("Notebook/scaler_rfloans.sav", 'rb'))
        user_scaled = scaler.transform(user_df)
        rf_model = pickle.load(open('Notebook/finalized_rfloans.sav', 'rb'))
        user_prediction = rf_model.predict(user_scaled)

        print(user_prediction)
        if int(user_prediction) == 0:
            message = "You did not get the loan!"
            image = "https://image.shutterstock.com/image-illustration/red-seal-imprint-loan-denied-260nw-311583383.jpg"
        else:
            message = "Huzzah! you got the loan"
            image = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSkG249Z0__YtoOsxIXUnRe_dRgpLo_oz3oxg&usqp"


        result = {
            "message": message,
            "image": image,
        }
        print(result)
    
        return render_template('form2.html', result=result)
    else:
        return render_template('form2.html', result={})



if __name__ == "__main__":
    app.run(debug=True)
