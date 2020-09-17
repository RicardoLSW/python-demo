from urllib import request
import re
from outputLog import outputLog


class Crawler:
    def __init__(self, url, user_agent):
        self.request = None
        self.response = None
        self.url = url
        self.user_agent = user_agent
        self.logPath = 'crawlerLog'

    def get_html(self):
        self.request = request.Request(self.url)
        self.request.add_header('User-Agent', self.user_agent)
        self.response = request.urlopen(self.request).read()
        return self.response

    def get_img_url(self):
        response = self.get_html()
        reg = r'src="(.*?\.jpg)"'
        img = re.compile(reg)
        html = response.decode('gbk')
        img_list = re.findall(img, html)
        for item in img_list:
            self.output_log(item)

    def output_log(self, log_message: str):
        """记录日志"""
        outputLog.OutputLog(self.logPath, 'a+', log_message)


if __name__ == '__main__':
    c = Crawler('http://www.4399.com/',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/85.0.4183.102 Safari/537.36')
    c.get_img_url()
