ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN pip install scipy statsmodels && \
    ln -s /usr/local/lib/python3.12/site-packages/scipy /usr/local/lib/python3.12/site-packages/scipy && \
    ln -s /usr/local/lib/python3.12/site-packages/statsmodels /usr/local/lib/python3.12/site-packages/statsmodels

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]
