import pickle
from flask import Flask, request, render_template
import numpy as np

# Initialize Flask
application = Flask(__name__)
app = application  # for hosting compatibility

# Load Ridge regression model and scaler
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

# Index route (landing page)
@app.route('/')
def index():
    return render_template('index.html')

# Home route (prediction form page)
@app.route('/home')
def home():
    return render_template('home.html')

# Prediction route
@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    try:
        # Get inputs from form
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        # Prepare input for scaling and prediction
        input_data = {
            'Temperature': Temperature,
            'RH': RH,
            'Ws': Ws,
            'Rain': Rain,
            'FFMC': FFMC,
            'DMC': DMC,
            'ISI': ISI,
            'Classes': Classes,
            'Region': Region
        }

        # Scale and predict
        new_data_scaled = standard_scaler.transform(
            [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
        )
        prediction = ridge_model.predict(new_data_scaled)[0]

        # Render result page
        return render_template(
            'result.html',
            input_data=input_data,
            prediction_text=f"{round(prediction, 2)}"
        )

    except Exception as e:
        return f"Error occurred: {str(e)}"

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
