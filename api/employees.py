import json
import os
import random

from requests_toolbelt import MultipartEncoder

from api.base import Base
from tests import PROJ_DIR


class Employees(Base):
    def __init__(self, client=None):
        super().__init__(client)

    def remove_employee(self, emp_number=None):
        resp = self.sess.get("http://hrm-online.portnov.com/symfony/web/index.php/pim/viewEmployeeList")
        csrf_token = self.extract_token(resp.text, 'defaultList')

        data = f"defaultList%5B_csrf_token%5D={csrf_token}"
        data = f"{data}&chkSelectRow%5B%5D={emp_number}" if emp_number else data
        return self.sess.post(url='http://hrm-online.portnov.com/symfony/web/index.php/pim/deleteEmployees', headers=self.headers, data=data)

    def get_all_employees(self):
        url = 'http://hrm-online.portnov.com/symfony/web/index.php/pim/getEmployeeListAjax'
        headers = {'Accept': 'application/json'}   # optional

        resp = self.sess.get(url=url, headers=headers)
        return json.loads(resp.text)


    def add_employee(self, first_name, last_name, emp_id=None):
        url = 'http://hrm-online.portnov.com/symfony/web/index.php/pim/addEmployee'
        resp = self.sess.get(headers={}, url=url)

        csrf_token = self.extract_token(resp.text)

        emp_number = str(emp_id if emp_id is not None else random.randrange(10000, 9999999))

        avatar_photo = os.path.join(PROJ_DIR, 'test_data', 'avatar.jpeg')

        with open(avatar_photo, 'rb') as file:
            multi_data = MultipartEncoder(
                fields={
                    'firstName': first_name,
                    # 'middleName': '',
                    'lastName': last_name,
                    'employeeId': emp_number,
                    'photofile': ('my_photo', file, 'image/jpeg'),
                    # 'user_name': '',
                    # 'user_password': '',
                    # 're_password': '',
                    'status': 'Enabled',
                    'empNumber': emp_number,
                    '_csrf_token': csrf_token
            })

            print("emp_number: ", emp_number)
            headers = {'Content-Type': multi_data.content_type}
            return self.sess.post(url=url, headers=headers, data=multi_data.to_string())

    def add_emergency_contact(self):
        pass
