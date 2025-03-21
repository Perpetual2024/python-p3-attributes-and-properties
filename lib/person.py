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
    def __init__(self, name, job):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            raise TypeError("Name must be a string between 1 and 25 characters.")
        self._name = value

    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            raise TypeError("Job must be a string between 1 and 25 characters.")
        if value not in APPROVED_JOBS:
            raise ValueError("Job must be in list of approved jobs")