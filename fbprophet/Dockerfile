# Usa la imagen Prophet de Docker Hub como base
FROM safakcirag/fbprophet

# Instalar Flask para crear la API
RUN pip install flask

# Copiar el archivo de la API al contenedor
COPY prophet_api.py /app/prophet_api.py
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

# Exponer el puerto de la API
EXPOSE 5000

# Ejecutar el script de inicio
CMD [ "/app/run.sh" ]


