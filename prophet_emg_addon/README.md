Addon que implementa una API para hacer llamadas a Prophet

Ejemplo de uso
```bash
curl -X POST http://<Raspberry_Pi_IP>:5000/forecast -H "Content-Type: application/json" -d '{"data": [{"ds": "2024-01-01", "y": 10}, {"ds": "2024-01-02", "y": 15}]}'
```

Ejemplo de uso desde Python

```python
import requests
import json

# URL de la API del add-on
url = "http://homeassistant.local:5000/forecast"  # Cambia 'homeassistant.local' según sea necesario

# Datos de ejemplo en el formato esperado (fechas y valores)
data = {
    "data": [
        {"ds": "2024-01-01", "y": 10},
        {"ds": "2024-01-02", "y": 15},
        {"ds": "2024-01-03", "y": 13},
        {"ds": "2024-01-04", "y": 18}
    ]
}

# Hacer la solicitud POST
response = requests.post(url, json=data)

# Verificar la respuesta
if response.status_code == 200:
    forecast = response.json()
    print("Forecast:")
    print(json.dumps(forecast, indent=2))
else:
    print("Error:", response.status_code)
    print(response.text)
```