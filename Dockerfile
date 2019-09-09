FROM nginx:alpine
RUN apk update && apk add python3

RUN pip3 install --no-cache jinja2

COPY bin/build_config.py /usr/bin/build_config.py

CMD python3 /usr/bin/build_config.py /etc/nginx/conf.d/default.conf.tmp; python3 /usr/bin/build_config.py /etc/nginx/conf.d/default.conf.tmp > /etc/nginx/conf.d/default.conf; nginx -g 'daemon off;';

