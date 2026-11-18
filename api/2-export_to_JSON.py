#!/usr/bin/python3
"""
Fetch all TODO tasks of an employee from the JSONPlaceholder REST API
and export them to a JSON file named USER_ID.json.

Usage: ./2-export_to_JSON.py <employee_id>
"""
import json
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com"


def main():
    """Write every task of the given employee to USER_ID.json."""
    employee_id = int(sys.argv[1])

    user = requests.get("{}/users/{}".format(API_URL, employee_id)).json()
    todos = requests.get("{}/todos".format(API_URL),
                         params={"userId": employee_id}).json()
    username = user.get("username")

    tasks = [{"task": task.get("title"),
              "completed": task.get("completed"),
              "username": username} for task in todos]

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file)


if __name__ == "__main__":
    main()
