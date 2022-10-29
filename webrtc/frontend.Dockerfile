FROM node:16

WORKDIR /frontend

COPY ./frontend /frontend

CMD ["sh", "/frontend/entrypoint.sh"]
