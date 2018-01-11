# coding=utf-8
from utils import *
from config import PROXY_SITES


for url in PROXY_SITES:
    try:
        s = requests.Session()
        s.headers.update({'user-agent': get_user_agent()})
        res = s.get(url)
        if(res.status_code != 200):
            print(res.url)
            continue
    except:
        print("exception url is "+url)
        continue

print("success!");
import pdb; pdb.set_trace()

