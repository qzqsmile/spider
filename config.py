import re

PROXY_SITES = [
    # 'http://cn-proxy.com',
    'http://www.xicidaili.com',
    # 'http://www.kuaidaili.com/free',
    'https://www.kuaidaili.com/free/intr',
    'http://www.proxylists.net/?HTTP',
    'http://31f.cn',
    'http://www.coobobo.com',
    'http://www.kxdaili.com'
    # 'http://proxy.mimvp.com',
]


REFEREE_LIST = [
    # 'http://www.google.com/',
    'http://www.bing.com/',
    'http://www.baidu.com/'
]

DB_HOST = 'localhost'
DB_PORT = 27017
DATABASE_NAME = 'weixinspider'

TIMEOUT = 5

# PROXY_REGEX = re.compile('[0-9]+(?:\.[0-9]+){3}:\d{2,4}')
PROXY_REGEX = re.compile('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')

