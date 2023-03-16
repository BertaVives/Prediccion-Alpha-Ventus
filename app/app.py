from flask import Flask, request, jsonify, session, url_for, redirect, render_template
import joblib
import os

import numpy as np

# importar el formulario custom
from power_form import PowerForm

# Importar los ficheros serializados
regression_loaded = joblib.load("./src/model/knn_model.pkl")

# Creamos la función de prediccion
def make_prediction(model, sample_json):

    # recoger los valores del formulario
    WindSpeed = sample_json['WindSpeed']
    WindDirection = sample_json['WindDirection']
    YawAngle = sample_json['YawAngle']
    Estacion = sample_json['Estacion']
    MomentoDia = sample_json['MomentoDia']
    Año = sample_json['Año']

    # modificamos las necesarias para hacer la prediccion
    WindSpeed_log = np.log(WindSpeed+1)
    Sin_WD = np.sin(2 * np.pi * WindDirection / 360)
    Cos_WD = np.cos(2 * np.pi * WindDirection / 360)
    Sin_Yaw = np.sin(2 * np.pi * YawAngle / 360)
    Cos_Yaw = np.cos(2 * np.pi * YawAngle / 360)
    Estacion_num = (Estacion=='primavera')*0+(Estacion=='verano')*1+(Estacion=='otoño')*2+(Estacion=='inviero')*3
    MomentoDia_num = (MomentoDia=='mañana')*0+(MomentoDia=='tarde')*1+(MomentoDia=='noche')*2+(MomentoDia=='madrugada')*3

    # Creamos un vector de input
    power = [[WindSpeed_log, Sin_WD, Cos_WD, Sin_Yaw, Cos_Yaw, Estacion_num, MomentoDia_num, Año]]

    # Realizamos la prediccion
    prediction = model.predict(power)
    return prediction


# Definición de la Web App
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# Definimos la plantilla de homepage /
@app.route("/", methods=['GET','POST'])

# Creamos el formulario
def index():
    # estructuramos el formulario
    form = PowerForm()
    if form.validate_on_submit():
        session['WindSpeed'] = form.WindSpeed.data
        session['WindDirection'] = form.WindDirection.data
        session['YawAngle'] = form.YawAngle.data
        session['Estacion'] = form.Estacion.data
        session['MomentoDia'] = form.MomentoDia.data
        session['Año'] = form.Año.data
        return redirect(url_for('prediction'))
    return render_template('home.html', form=form)

# Creamos la plantilla de la página prediction
@app.route('/prediction')
def prediction():
    content = {'WindSpeed': float(session['WindSpeed']), 'WindDirection': float(session['WindDirection']),
               'YawAngle': float(session['YawAngle']), 'Estacion': session['Estacion'],
               'MomentoDia': session['MomentoDia'], 'Año': int(session['Año'])}
    results = make_prediction(regression_loaded, content)
    return render_template('prediction.html', results=results)
if __name__ == '__main__':
    #port = int(os.environ.get('PORT', 8080))
    app.run(host='127.0.0.1', port=8080)
    #app.run()

