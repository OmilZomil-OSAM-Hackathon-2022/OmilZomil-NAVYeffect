FROM node:16

WORKDIR /frontend
RUN chmod -R 777 /frontend

COPY ./frontend/entrypoint.sh /entrypoint.sh
RUN chmod u+x /entrypoint.sh
CMD ["sh", "/entrypoint.sh"]
