#######################
#--- Get Data ---#
#######################
'''
comentario largo o descripción de la operación a realizar

'''
# Importar librerías
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

import joblib

# Importamos los datos
data = pd.read_csv('./src/data/processed/prepared_data.csv', index_col=0)
print(data.head(10))


#######################
#--- DataWrangling ---#
#######################

# Matriz de features 
X = data.drop(columns='ActivePower')

# Variable target
y = data['ActivePower']
print("--- Paso X-y executed ---")

# Creamos la instancia de LabelEncoder
num_estacion = []
for i in X['Estacion']:
    i = (i=='primavera')*0+(i=='verano')*1+(i=='otoño')*2+(i=='inviero')*3
    num_estacion.append(i)
X['Estacion'] = num_estacion

num_momento = []
for i in X['MomentoDia']:
    i = (i=='mañana')*0+(i=='tarde')*1+(i=='noche')*2+(i=='madrugada')*3
    num_momento.append(i)
X['MomentoDia'] = num_momento
print("--- LabelEncoder executed ---")

# Normalizamos las variables numericas
X['WindSpeed'] = np.log(X['WindSpeed']+1)


#######################
#---    Modeling   ---#
#######################

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3, 
                                                    random_state=17)

print("--- Train and Test executed ---")


# Train Model
model = KNeighborsRegressor()
model.fit(X_train, y_train)
print("--- Training executed ---")

# Prediction
y_pred = model.predict(X_test)
print("--- Prediction executed ---")

# Scoring
score = round(model.score(X_train, y_train), 4)
print("Score del modelo (R^2):", score)


# Serialización del modelo
joblib.dump(model, "./src/model/knn_model.pkl")

#######################
#---    Testing   ---#
#######################

# classifier_loaded = joblib.load("saved_models/knn_iris.pkl")
# encoder_loaded = joblib.load("saved_models/iris_label_encoder.pkl")

# # Prediction en real-time
# X_manual_test = [[20.1, 20, 100, 100]]
# print("X_manual_test", X_manual_test)

# prediction_raw = classifier_loaded.predict(X_manual_test)
# print("Prediction_raw", prediction_raw)

# # Transformar - decoder de la clase
# prediction_real = encoder_loaded.inverse_transform(
#     classifier.predict(X_manual_test)
# )
# print("Prediction_real", prediction_real)