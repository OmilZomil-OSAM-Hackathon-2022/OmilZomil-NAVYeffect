FROM node:16

WORKDIR /frontend

COPY ./frontend/entrypoint.sh /entrypoint.sh
RUN chmod u+x /entrypoint.sh
CMD ["sh", "/entrypoint.sh"]
