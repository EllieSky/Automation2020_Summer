from api.base import Base

class Jobs(Base):
    def __init__(self, client=None):
        super().__init__(client)

    def add_job_title(self):
        pass

    def remove_job_title(self):
        pass