#!/usr/bin/python3
'''
Using what you did in the task #0, extend your Python script
to export data in the JSON format.
'''
import json
import requests

if __name__ == "__main__":
    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    tasks = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    storage = {}

    for user in users:
        em_id = user.get("id")
        username = user.get("username")
        all = []

        for task in tasks:
            if (task.get("userId") == em_id and task.get("completed")):
                tmp = {}
                tmp["task"] = task.get("title")
                tmp["completed"] = task.get("completed")
                tmp["username"] = username
                all.append(tmp)

        storage[em_id] = all

    with open("todo_all_employees.json", 'w+') as jsonfile:
        json.dump(storage, jsonfile)
