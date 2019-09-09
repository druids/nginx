# Nginx

## Instalation

Prepare your nginx config template in Jinja2 format:

```
server {
    listen {{ STATIC_URL|port }};
    server_name {{ STATIC_URL|domain }};

    charset utf-8;
    client_max_body_size 10M;

    location /media  {
        alias /usr/src/app/var/media;
    }

    location /static {
        alias /usr/src/app/var/static;
    }
}
```

Run docker with volume:

```
docker run pydruids/nginx -v './default.conf.tmp:/etc/nginx/conf.d/default.conf.tmp'
```