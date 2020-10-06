import json
import os
import unittest
import random
import requests
import csv
from parameterized import parameterized

from faker import Faker

from api.client import HRM
from api.employees import Employees
from api.jobs import Jobs
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

        emp_list = api.employee.get_all_employees()
        api.jobs.authenticate()

        # random_index = random.randrange(len(emp_list))
        ## OR
        random_record = random.choice(emp_list)
        if random_record['name'] == 'Admin Admin':
            emp_list.remove(random_record)
            random_record = random.choice(emp_list)

        result = api.employee.remove_employee(random_record['id'])

        emp_list_after = api.employee.get_all_employees()

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
        resp = api.employee.remove_employee(input)

        self.assertIn(expected_output, resp.text)

    # remove twice the same empNumber
    # remove none existent


    def test_create_emp(self):
        self.data = Faker()
        first = self.data.first_name()
        last = self.data.last_name()
        api = HRM()
        api.authenticate()
        resp = api.employee.add_employee(first, last)
        emp_number = resp.url.split('/')[-1]
        all_emp = api.employee.get_all_employees()
        self.assertIn({"name": first + " " + last, "id": emp_number}, all_emp)


    def test_client(self):
        # can work with just employee api
        emp_client = Employees()
        emp_client.authenticate()
        emp_client.get_all_employees()

        # or with just job api
        job_client = Jobs()
        job_client.authenticate()
        job_client.add_job_title()

        # or with ALL api
        client = HRM()
        client.authenticate()
        client.employee.add_employee("Bob", "Anderson")
        client.jobs.remove_job_title()

        # Can also use any preexisting client to instantiate another client, and share the session
        client2 = HRM(emp_client)

if __name__ == '__main__':
    unittest.main()
