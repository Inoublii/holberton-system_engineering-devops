#!/usr/bin/python3
'''
Python script that use API,
to export data in the JSON format..
Records all tasks from all employees
'''

import json
import requests

if __name__ == "__main__":
    url = requests.get("http://jsonplaceholder.typicode.com/users").json()
    users = requests.get(url, verify=False).json()
    username_doc = {}
    user_doc = {}
    for user in users:
        uid = user.get("id")
        user_doc[uid] = []
        username_doc[uid] = user.get("username")
    url = "https://jsonplaceholder.typicode.com/todos"
    todo = requests.get(url, verify=False).json()
    [user_doc.get(t.get("userId")).append({"task": t.get("title"),
                                           "completed": t.get("completed"),
                                           "username": username_doc.get(
                                               t.get("userId"))})
     for t in todo]
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(user_doc, jsonfile)
