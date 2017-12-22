import re

PROXY_SITES = [
    # 'http://cn-proxy.com',
    'http://www.xicidaili.com',
    # 'http://www.kuaidaili.com/free',
    # 'http://www.proxylists.net/?HTTP',
    # www.youdaili.net的地址随着日期不断更新
    # 'http://www.youdaili.net/Daili/http/4565.html',
    # 'http://www.youdaili.net/Daili/http/4562.html',
    # 'http://www.kuaidaili.com',
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

