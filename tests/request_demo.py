import unittest
import requests

from api.client import HRM


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

    def test_auth(self):
        api = HRM()
        api.authenticate()

        # emp_list = api.get_all_employees()

        api.remove_employee(3289)

        # emp_list_after = api.get_all_employees()

        # assertTrue(<employee number is no longer in the list)

    # remove twice the same empNumber
    # remove none existent




if __name__ == '__main__':
    unittest.main()
