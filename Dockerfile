FROM alpine:latest
RUN apk add --update hugo bash nginx imagemagick && rm -rf /var/cache/apk/*
RUN mkdir -p /tmp/nginx/client-body

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Build static site
RUN mkdir -p /tmp/hugo-site
COPY site /usr/share/hugo/site
#RUN cd /tmp/hugo-site && hugo -d /usr/share/nginx/html

#CMD bash
WORKDIR /usr/share/hugo/site
EXPOSE 1313
CMD ["hugo", "server", "--bind=0.0.0.0"]
#CMD ["nginx", "-g", "daemon off;"]