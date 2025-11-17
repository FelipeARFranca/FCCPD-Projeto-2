FROM alpine:3.19


RUN apk add --no-cache curl bash


WORKDIR /app
COPY request_loop.sh ./
RUN chmod +x request_loop.sh


CMD ["/app/request_loop.sh"]