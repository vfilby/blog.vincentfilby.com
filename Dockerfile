FROM alpine:latest
RUN apk add --update hugo bash nginx imagemagick && rm -rf /var/cache/apk/*
RUN mkdir -p /tmp/nginx/client-body

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Build static site
COPY site /usr/share/hugo/site
WORKDIR /usr/share/hugo/site
RUN hugo -d /usr/share/nginx/html


EXPOSE 80
#CMD ["hugo", "server", "--bind=0.0.0.0"]
CMD ["nginx", "-g", "daemon off;"]
