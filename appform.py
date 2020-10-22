from flask import Flask, render_template, request, redirect, url_for
#from werkzeug import secure_filename
import pickle
import numpy as np
import pandas

app = Flask(__name__)


@app.route('/upload')
def upload_file():
    return render_template('form.html')


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.form['Loan Application Form']
        # f.save(secure_filename(f.Loan_Application_Form))
        return 'file uploaded successfully'
    return render_template('form.html')


# @app.route('/', methods=['POST', 'GET'])
def preprocess(input_data):
    df = input_data.dropna(axis='columns', how='all').copy()
    df = df.dropna(axis='index', how='any')
    df = pd.get_dummies(df, columns=["Gender", "Married", "Education",
                                     "Self_Employed", "Property_Area", "Loan_Status"], drop_first=True)
    scaler = pickle.load(open("scaler_rfloans.sav", 'rb'))
    df_scaler = scaler.transform(df)
    df_scaler = df_scaler[["Credit_History", "ApplicantIncome",
                           "Loan_Amount_Term", "CoapplicantIncome"]]
    return df_scaler


def runmodel(input_data):
    input_data = preprocess(input_data)
    rf_model = pickle.load(open('finalized_rfloans.sav', 'rb'))
    y_predict = rf_model.predict(input_data)
    return y_predict

@app.route('/predictions', methods=['GET', 'POST'])
def prediction():
    # get user responses of each question from the html form
    user_input = request.form.to_dict()
    user_input = list(user_input.values())
    user_input = list(map(int, user_input))
    prediction = runmodel(input_data)
   # user prediction is going to be a 0 or a 1
    if int(result) == 0:
        prediction = message = "You did not get the loan!"
        image = "https://image.shutterstock.com/image-illustration/red-seal-imprint-loan-denied-260nw-311583383.jpg"
    else:
        message = "Huzzah! you got the loan"
        image = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSkG249Z0__YtoOsxIXUnRe_dRgpLo_oz3oxg&usqp"
    prediction_dict = {"message": message, "image": image}
    # after getting all of the data needed for prediction, you assemble the data
    # in a vector
    user_data = np.array[{"Gender": {"Male": 1, "Female": 0},
                          "Marital Status": {"Single": 0, "Married": 1},
                          "Emplpoyment": {"Self-Employed": 1,
                                          "Not Self_Employed": 0},
                          "Income": {'ApplicantIncome': 1, 'CoapplicantIncome': 0},
                          'Credit_History': {"Yes": 1, "No": 0},
                          'Education': {"Graduate": 1, "Not Graduate": 0},
                          "Property_Area": {'Rural': 0, "Urban": 1, "Semiurban": 2},
                          'LoanAmount': {"Yes": 1, "No": 0},
                          'Loan_Amount_Term': {'Yes': 1, "No": 0}}]
    # make it a 1-D numpy array
    # load your model and scaler
    scaler = joblib.load("scalingfunction.sav")
    user_scaled = scaler.transform(user_data)
    user_prediction = model.predict(user_scaled)
    # returns the whole prediction string value when user submits the form
    return render_template('results.html', prediction=prediction_dict)


if __name__ == "__main__":
    app.run(debug=True)
