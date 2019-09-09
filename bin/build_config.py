import os
import sys

from urllib.parse import urlparse

from jinja2 import Environment, Template, FileSystemLoader


def get_domain(url):
    return urlparse(url).hostname


def get_port(url):
    parsed_url = urlparse(url)
    if parsed_url.port:
        return parsed_url.port
    elif parsed_url.scheme == 'http':
        return 80
    else:
        return 443


template_loader = FileSystemLoader(searchpath='/')

env = Environment(loader=template_loader)
env.filters['domain'] = get_domain
env.filters['port'] = get_port

template = env.get_template(sys.argv[1])
print(template.render(**os.environ))
