from requests.exceptions import RequestException

from utils import fetch


def check_proxy(p):
    try:
        res = fetch('http://weixin.sogou.com', proxy=p['address'])
    except RequestException:
        p.delete()
