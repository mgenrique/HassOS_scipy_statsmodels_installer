# Usa la imagen `arvethir/prophet` como base
FROM arvethir/prophet:1.0

# Instalar Flask para la API (opcional)
RUN pip install flask

# Copiar los archivos de la API
COPY prophet_api.py /app/prophet_api.py
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

# Exponer el puerto de la API
EXPOSE 5000

# Ejecutar el script de inicio
CMD [ "/app/run.sh" ]



