#!/usr/bin/python3
'''
Python script that use API,
to export data in the JSON format..
'''
import json
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    emp_name = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                            .format(emp_id)).json().get("username")
    done = []
    x = requests.get("http://jsonplaceholder.typicode.com/todos").json()

    for todos in x:
        if (todos.get("userId") == int(emp_id)):
            tmp = {}
            tmp["task"] = todos.get("title")
            tmp["completed"] = todos.get("completed")
            tmp["username"] = emp_name
            done.append(tmp)

    with open("{}.json".format(emp_id), 'w+') as jsonfile:
        json.dump({emp_id: done}, jsonfile)
