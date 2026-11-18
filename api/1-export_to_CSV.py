#!/usr/bin/python3
"""
Fetch all TODO tasks of an employee from the JSONPlaceholder REST API
and export them to a CSV file named USER_ID.csv.

Usage: ./1-export_to_CSV.py <employee_id>
"""
import csv
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com"


def main():
    """Write every task of the given employee to USER_ID.csv."""
    employee_id = int(sys.argv[1])

    user = requests.get("{}/users/{}".format(API_URL, employee_id)).json()
    todos = requests.get("{}/todos".format(API_URL),
                         params={"userId": employee_id}).json()
    username = user.get("username")

    with open("{}.csv".format(employee_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, username,
                             task.get("completed"), task.get("title")])


if __name__ == "__main__":
    main()
