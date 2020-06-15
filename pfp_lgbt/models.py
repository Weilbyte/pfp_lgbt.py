class Request(object):
    def __init__(self, endpoint, headers, method, body, files):
        self.endpoint = endpoint
        self.headers = headers
        self.method = method
        self.body = body
        self.files = files

class Flag(object):
    def __init__(self, name, default_alpha=255, tooltip=None, image=None):
        self.name = name 
        self.default_alpha = default_alpha
        self.tooltip = tooltip
        self.image = image

types = {'circle', 'overlay', 'square', 'background'}
styles = {'solid', 'gradient'}
formats = {'png', 'jpg'}
mimes = {'image/jpeg', 'image/png', 'image/gif', 'image/webp', 'image/jpg'}
