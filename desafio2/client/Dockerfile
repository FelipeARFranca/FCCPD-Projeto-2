FROM alpine:3.19
RUN apk add --no-cache postgresql-client bash
WORKDIR /app
COPY read_data.sh ./
RUN chmod +x read_data.sh
CMD ["/app/read_data.sh"]