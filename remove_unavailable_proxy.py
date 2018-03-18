from requests.exceptions import RequestException

from utils import fetch


def check_proxy(p):
    try:
        res = fetch('http://weixin.sogou.com/weixin?query=python&type=2&page=1', proxy=p['address'])
        if len(res.text) < 10000:
            p.delete()
    except RequestException:
        p.delete()
