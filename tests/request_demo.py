import json
import os
import unittest
import random
import requests
import csv
from parameterized import parameterized

from api.client import HRM
from tests import PROJ_DIR

def get_data_from_json():
    data_file = os.path.join(PROJ_DIR, 'test_data', 'data.json')
    with open(data_file, newline='') as file:
        json_data = json.loads(file.read())
        j = list()
        for i in json_data:
            j.append((i['test_name'], i['input'], i['expected_output']))
        return j




def get_data_from_csv():
    data_file = os.path.join(PROJ_DIR, 'test_data', 'data.csv')
    with open(data_file, newline='') as file:
        reader = csv.reader(file)
        next(reader)
        return list(map(tuple,reader))

        # one line that does exactly the same thing as
        # j = list()
        # for i in reader:
        #     k = tuple(i)
        #     j.append(k)


class RequestsDemo(unittest.TestCase):

    def test_get_google(self):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
        header = {'user-agent': user_agent}

        response = requests.get('http://www.google.com', headers=header)
        self.assertEqual(200, response.status_code)

        file = open("result.html", "w")
        file.write(response.text)
        file.close()

    def test_remove_emp_positive(self):
        api = HRM()
        api.authenticate()

        emp_list = api.get_all_employees()

        # random_index = random.randrange(len(emp_list))
        ## OR
        random_record = random.choice(emp_list)
        if random_record['name'] == 'Admin Admin':
            emp_list.remove(random_record)
            random_record = random.choice(emp_list)

        result = api.remove_employee(random_record['id'])

        emp_list_after = api.get_all_employees()

        # print(f"Deleted employee named {random_record['name']}, number {random_record['id']}")

        self.assertNotIn(random_record, emp_list_after)

    # @parameterized.expand([
    #     ('remove_non_existing_employee', '0000001', 'Credentials Required'),
    #     ('non_int_data_type', 'abcdef', 'Credentials Required'),
    #     ('negative_emp_number', '-99999', 'Credentials Required'),
    #     ('empty_emp_number', '', 'Delete records?'),
    #     ('space_emp_number', ' ', 'Credentials Required'),
    #     ('none_emp_number', None, 'Delete records?')
    # ])
    @parameterized.expand(get_data_from_json)
    def test_remove_employee_api(self, test_name, input, expected_output):
        api = HRM()
        api.authenticate()
        # 'message warning'
        if input.strip() == 'None' or input.strip() == 'null':
            input = None
        resp = api.remove_employee(input)

        self.assertIn(expected_output, resp.text)

    # remove twice the same empNumber
    # remove none existent




if __name__ == '__main__':
    unittest.main()
