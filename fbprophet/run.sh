#!/usr/bin/with-contenv bashio

echo "Starting Prophet API service..."
python3 /app/prophet_api.py &

echo "Starting Jupyter Notebook..."
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
