# app.py
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        age = float(request.form['age'])
        sex = float(request.form['sex'])
        cigs = float(request.form['cigsPerDay'])
        chol = float(request.form['totChol'])
        bp = float(request.form['sysBP'])
        glucose = float(request.form['glucose'])

        features = np.array([[age, sex, cigs, chol, bp, glucose]])
        features = scaler.transform(features)
        prediction = model.predict(features)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
