ARG BUILD_FROM
FROM ${BUILD_FROM}

# Paso 1: Instalar pip
RUN apk add --no-cache py3-pip

# Paso 2: Instalar herramientas de compilación necesarias
RUN apk add --no-cache build-base gfortran

# Paso 3: Instalar scipy usando pip
RUN pip install scipy

# Paso 4: Limpiar las herramientas de compilación para reducir el tamaño de la imagen
RUN apk del build-base gfortran py3-pip

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]
