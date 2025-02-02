FROM node:18 AS builder

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install

COPY . .

EXPOSE 5713
ENTRYPOINT ["npm", "run", "dev", "--", "--port=5713", "--host=0.0.0.0"]