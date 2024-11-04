# Usa la imagen `peterpeerdeman/docker-prophet-arm` como base
FROM peterpeerdeman/docker-prophet-arm

# Instalar Flask (opcional si necesitas una API)
RUN pip install flask

# Copiar el archivo de la API o cualquier otro archivo necesario
COPY prophet_api.py /app/prophet_api.py
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

# Exponer el puerto de la API
EXPOSE 5000

# Ejecutar el script de inicio
CMD [ "/app/run.sh" ]



