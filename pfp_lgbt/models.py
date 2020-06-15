class Request(object):
    def __init__(self, endpoint, headers, method, body, files):
        self.endpoint = endpoint
        self.headers = headers
        self.method = method
        self.body = body
        self.files = files

class Flag(object):
    def __init__(self, name, default_alpha, tooltip):
        self.name = name 
        self.default_alpha = default_alpha
        self.tooltip = tooltip

