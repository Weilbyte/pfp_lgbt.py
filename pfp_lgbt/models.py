class Request(object):
    def __init__(self, endpoint, headers, method, body, files):
        self.endpoint = endpoint
        self.headers = headers
        self.method = method
        self.body = body
        self.files = files

