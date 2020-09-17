from urllib import request


class Crawler:
    def __init__(self, url, user_agent):
        self.request = None
        self.response = None
        self.url = url
        self.user_agent = user_agent

    def get_html(self):
        self.request = request.Request(self.url)
        self.request.add_header('User-Agent', self.user_agent)
        self.response = request.urlopen(self.request)
        print(self.response.read())
        return self.response.read()


if __name__ == '__main__':
    c = Crawler('http://www.4399.com/',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/85.0.4183.102 Safari/537.36')
    c.get_html()
