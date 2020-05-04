#!/usr/bin/python3
'''
Python script that use API,
to export data in the JSON format..
'''
import requests
import sys
import json

if __name__ == "__main__":
    emp_id = sys.argv[1]
    emp_name = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                        .format(emp_id)).json().get("username")
    sums = 0
    done = []
    x = requests.get("http://jsonplaceholder.typicode.com/todos").json()

    for todos in x:
        if (todos.get("userId") == int(emp_id)):
            tmp = {}
            tmp["task"] = todos.get("title")
            tmp["completed"] = todos.get("completed")
            tmp["username"] = emp_name
            all.append(tmp)

    with open("{}.json".format(emp_id), 'w+') as jsonfile:
        json.dump({emp_id: all}, jsonfile)
