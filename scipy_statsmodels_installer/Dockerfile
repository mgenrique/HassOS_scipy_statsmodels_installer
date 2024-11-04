ARG BUILD_FROM
FROM ${BUILD_FROM}

# Añadir repositorio de edge/community para py3-statsmodels
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
    apk update && \
    apk add --no-cache py3-scipy py3-statsmodels

# Copiar el script de ejecución
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]



