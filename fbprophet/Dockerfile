# Usa la imagen Prophet de Docker Hub como base
FROM safakcirag/fbprophet

# Instalar Flask para crear la API
RUN pip install flask

# Copiar los archivos necesarios al contenedor
COPY prophet_api.py /app/prophet_api.py
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

# Exponer puertos para Flask y Jupyter Notebook
EXPOSE 5000
EXPOSE 8888

# Ejecutar el script de inicio
CMD [ "/app/run.sh" ]


