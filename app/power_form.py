from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class PowerForm(FlaskForm):
    # input text
    WindSpeed = StringField('Wind speed [m/s]')
    WindDirection = StringField('Wind direction [°]')
    YawAngle = StringField('Yaw angle [°]')
    Estacion = StringField('Season')
    MomentoDia = StringField('Time of the day')
    Año = StringField('Year')

    # submit boton que llama la función make_prediction
    submit = SubmitField("Predict")