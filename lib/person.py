#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="John", job="Admin"):
        self.name = name
        self.job = job

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title() 
        else:
            print("Name must be string between 1 and 25 characters.")

    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self.set_name(name)

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        self.set_job(job)