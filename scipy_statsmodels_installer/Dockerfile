ARG BUILD_FROM
FROM ${BUILD_FROM}

# Instalar pip, herramientas de compilación y dependencias específicas para scipy
RUN apk add --no-cache py3-pip build-base gfortran musl-dev linux-headers openblas-dev

# Establecer variable de entorno para que scipy use OpenBLAS
ENV BLAS=/usr/lib/libopenblas.so.0
ENV LAPACK=/usr/lib/libopenblas.so.0

# Instalar scipy usando pip
RUN pip install scipy

# Limpiar las herramientas de compilación para reducir el tamaño de la imagen
RUN apk del build-base gfortran musl-dev linux-headers openblas-dev py3-pip

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]

