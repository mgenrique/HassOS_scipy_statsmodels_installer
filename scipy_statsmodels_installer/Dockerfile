ARG BUILD_FROM
FROM ${BUILD_FROM}

# Instalar scipy desde PyPI
RUN apk add --no-cache build-base gfortran && \
    pip install scipy && \
    apk del build-base gfortran

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]
