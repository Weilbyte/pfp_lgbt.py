from ratelimit import limits

from .throttle import RequestThrottle
from .models import Request, Flag
from .handlers import handleFlags

class Client(object):
    def __init__(self, host='https://api.pfp.lgbt/v3', user_agent='pfp_lgbt.py/0.1.0', key=None):
        self.host = host
        self.key = key
        self.headers = {
            'User-Agent': user_agent,
            'Accept': '*/*'
        }

        self.throttle = RequestThrottle()

    def flags(self):
        endpoint = f'{self.host}/flags'
        response = self.throttle.chew(Request(endpoint, self.headers, 'GET', None, None))
        return handleFlags(response)

    def icon(self, flag):
        endpoint = f'{self.host}/icon/{flag.name}'
        return self.throttle.chew(Request(endpoint, self.headers, 'GET', None, None))
