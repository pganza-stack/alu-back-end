#!/usr/bin/python3
"""
Fetch the TODO tasks of every employee from the JSONPlaceholder REST API
and export them to a JSON file named todo_all_employees.json.

Usage: ./3-dictionary_of_list_of_dictionaries.py
"""
import json
import requests

API_URL = "https://jsonplaceholder.typicode.com"


def main():
    """Write the tasks of all employees to todo_all_employees.json."""
    users = requests.get("{}/users".format(API_URL)).json()
    todos = requests.get("{}/todos".format(API_URL)).json()

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        all_tasks[str(user_id)] = [
            {"username": user.get("username"),
             "task": task.get("title"),
             "completed": task.get("completed")}
            for task in todos if task.get("userId") == user_id]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    main()
