import unittest
import requests


class RequestsDemo(unittest.TestCase):
    # made changes (by Carol)
    def test_get_google(self):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
        header = {'user-agent': user_agent}

        response = requests.get('http://www.google.com', headers=header)
        self.assertEqual(200, response.status_code)

        file = open("result.html", "w")
        file.write(response.text)
        file.close()


if __name__ == '__main__':
    unittest.main()
