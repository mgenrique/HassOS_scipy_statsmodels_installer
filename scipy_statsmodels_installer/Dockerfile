FROM python:3.12-alpine

# Instalar dependencias necesarias para el entorno de Home Assistant
RUN apk add --no-cache build-base gfortran musl-dev openblas-dev

# Instalar scipy y eliminar pip
RUN pip install scipy && apk del build-base gfortran musl-dev openblas-dev

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]


