ARG BUILD_FROM
FROM ${BUILD_FROM}

# Instalar pip y herramientas de compilación necesarias, instalar scipy, y luego limpiar
RUN apk add --no-cache build-base gfortran py3-pip && \
    pip install scipy && \
    apk del build-base gfortran py3-pip

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]

