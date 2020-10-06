from api.base import Base
from api.employees import Employees
from api.jobs import Jobs


class HRM(Base):
    def __init__(self, client=None):
        super().__init__(client)

        self.employee = Employees(self)
        self.jobs = Jobs(self)
        # self.admin = Admin()
        # self.leave = Leave()


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