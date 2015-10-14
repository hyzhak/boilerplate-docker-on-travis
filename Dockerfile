FROM node:4-onbuild

RUN npm install

# replace this with your application's default port
EXPOSE 8888