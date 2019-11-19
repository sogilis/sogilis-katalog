FROM node:10.15.3-alpine

COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . ./

ENTRYPOINT ["npm", "test"]
