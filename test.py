# coding=utf-8
from utils import *
from models import Proxy

s = requests.Session()
s.headers.update({'user-agent': get_user_agent()})
res = s.get('http://www.baidu.com')
import pdb; pdb.set_trace()
