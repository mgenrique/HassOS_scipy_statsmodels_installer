from flask import Flask, request, jsonify
from prophet import Prophet
import pandas as pd
from datetime import datetime

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Convertir los datos en un DataFrame
    df = pd.DataFrame(data)
    df['ds'] = pd.to_datetime(df['ds'])  # Asegurarse de que las fechas están en el formato correcto

    # Crear y entrenar el modelo Prophet
    model = Prophet()
    model.fit(df)

    # Hacer predicciones
    future = model.make_future_dataframe(periods=24, freq='H')  # Predice las próximas 24 horas
    forecast = model.predict(future)

    # Devolver el resultado como JSON
    forecast_json = forecast[['ds', 'yhat']].to_dict(orient='records')
    return jsonify(forecast_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
