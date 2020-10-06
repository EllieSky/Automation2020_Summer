import re

import requests


class Base:
    def __init__(self, client=None):
        self.client = client

        if client and isinstance(client, Base):
            self.sess = client.sess
        else:
            self.sess = requests.Session()

        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        # default header for all requests
        self.sess.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

    def extract_token(self, text: str, token_name='csrf_token'):
        regex = '([0-9a-z]{32})" id="' + token_name
        result = re.search(regex, text)
        return result.group(1)

    def authenticate(self, username='admin', password='password'):

        resp = self.sess.get("http://hrm-online.portnov.com/")
        csrf_token = self.extract_token(resp.text)

        data = f"_csrf_token={csrf_token}&txtUsername={username}&txtPassword={password}&Submit=LOGIN"
        return self.sess.post(url="http://hrm-online.portnov.com/symfony/web/index.php/auth/validateCredentials", headers=self.headers, data=data)

