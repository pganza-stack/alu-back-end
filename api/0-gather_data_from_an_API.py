#!/usr/bin/python3
"""
Fetch an employee's TODO list from the JSONPlaceholder REST API
and display how many of the tasks they have completed.

Usage: ./0-gather_data_from_an_API.py <employee_id>
"""
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com"


def main():
    """Print the TODO list progress of the given employee."""
    employee_id = int(sys.argv[1])

    user = requests.get("{}/users/{}".format(API_URL, employee_id)).json()
    todos = requests.get("{}/todos".format(API_URL),
                         params={"userId": employee_id}).json()

    done_tasks = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_tasks), len(todos)))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
