FROM alpine:latest
ARG PROTECTED_ASSET_KEY
RUN apk add --update hugo bash nginx imagemagick py-pygments openssl && rm -rf /var/cache/apk/*
RUN mkdir -p /tmp/nginx/client-body

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Build static site
COPY site /usr/share/hugo/site
WORKDIR /usr/share/hugo/site
RUN hugo -v -d /usr/share/nginx/html

# Unpack "protected" assets
WORKDIR /usr/share/hugo/site/static/galleria_themes
RUN openssl aes-256-ecb -d -in 9b67726fd76cdb263db0c3e93c88ec68.aes -pass pass:${PROTECTED_ASSET_KEY} | tar xz

EXPOSE 80
#CMD ["hugo", "server", "--bind=0.0.0.0"]
CMD ["nginx", "-g", "daemon off;"]
