ARG BUILD_FROM
FROM ${BUILD_FROM}

# Añadir el repositorio de community y actualizar la lista de paquetes
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
    apk update && \
    apk add --no-cache py3-scipy && \
    ln -s /usr/lib/python3.12/site-packages/scipy /usr/local/lib/python3.12/site-packages/scipy

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]
