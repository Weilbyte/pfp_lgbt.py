import time
import requests

from . import models 
from .models import Request

class RequestThrottle(object):
    def __init__(self):
        self.rateLimit = 2
        self.rateRemaining = 2
        self.rateReset = 0
    
    def __updateRatelimit(self, headers):
        if (('X-Ratelimit-Limit' in headers) and ('X-Ratelimit-Remaining' in headers) and ('X-Ratelimit-Reset' in headers)):
            self.rateLimit = int(headers['X-Ratelimit-Limit'])
            self.rateRemaining = int(headers['X-Ratelimit-Remaining'])
            self.rateReset = int(headers['X-Ratelimit-Reset'])

    def __isLimited(self):
        if ((time.time() - self.rateReset) > 0):
            self.rateRemaining = self.rateLimit
        if (self.rateRemaining > 0):
            return False 
        return True

    def chew(self, request): 
        if (self.__isLimited()):
            time.sleep(0.1)
            return self.chew(request)
        else:
            response = requests.request(request.method, headers=request.headers, url=request.endpoint, data=request.body, files=request.files)
            self.__updateRatelimit(response.headers)
            return response
