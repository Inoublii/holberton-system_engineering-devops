#!/usr/bin/python3
'''
Python script that use API,
for a given employee ID,
returns information about his/her TO DO list progress.
'''
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    emp_name = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                            .format(emp_id)).json().get("name")
    sums = 0
    done = []
    x = requests.get("http://jsonplaceholder.typicode.com/todos").json()

    for task in x:
        if (task.get("userId") == int(emp_id)):
            sums += 1
            if (task.get("completed")):
                done.append(task.get("title"))

    print("Employee {} is done with tasks({:d}/{:d}):"
          .format(emp_name, len(done), sums))

    for z in done:
        print("\t {}".format(z))
