import uuid

from datetime import datetime
from locust import HttpLocust, TaskSet, task


class AdminUserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    def login(self):
        self.client.post("/admin", {"username": "eli", "password": "password"})

    def logout(self):
        self.client.post("https://qa20.educationdive.com/admin/logout/", {"username": "eli", "password": "password"})


class WebUserBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def library(self):
        self.client.get("/library/")

    @task(3)
    def events(self):
        self.client.get("/events/")

    @task(4)
    def events_search(self):
        self.client.get("/events/?search=industry&month=Show+All")

    @task(5)
    def jobs(self):
        self.client.get("/jobs/")

    @task(6)
    def jobs_search(self):
        self.client.get("/jobs/?search=1&keywords=human&location=")


class WebsiteUser(HttpLocust):
    task_set = WebUserBehavior
    min_wait = 5000
    max_wait = 9000
