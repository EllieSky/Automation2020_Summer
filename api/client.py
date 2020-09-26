import requests
import re


class HRM:
    def __init__(self):
        self.sess = requests.Session()
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    def extract_token(self, text: str, token_name='csrf_token'):
        regex = '([0-9a-z]{32})" id="' + token_name
        result = re.search(regex, text)
        return result.group(1)

    def authenticate(self, username='admin', password='password'):

        resp = self.sess.get("http://hrm-online.portnov.com/")
        csrf_token = self.extract_token(resp.text)

        data = f"_csrf_token={csrf_token}&txtUsername={username}&txtPassword={password}&Submit=LOGIN"
        return self.sess.post(url="http://hrm-online.portnov.com/symfony/web/index.php/auth/validateCredentials", headers=self.headers, data=data)

    def remove_employee(self, emp_number):
        resp = self.sess.get("http://hrm-online.portnov.com/symfony/web/index.php/pim/viewEmployeeList")
        csrf_token = self.extract_token(resp.text, 'defaultList')

        data = f"defaultList%5B_csrf_token%5D={csrf_token}&chkSelectRow%5B%5D={emp_number}"
        self.sess.post(url='http://hrm-online.portnov.com/symfony/web/index.php/pim/deleteEmployees', headers=self.headers, data=data)


# client.authenticate()
# client.employee.remove_employee()
#
# ** EMPLOYEE **
# create
# delete
# get
# getall
# edit
# search
#
# USER
# create
# delete
# get
# getall
# edit
# search
#
# JOBS
# create
# delete
# get
# getall
# edit
# search
#
# POSITIONS
# create
# delete
# get
# getall
# edit
# search