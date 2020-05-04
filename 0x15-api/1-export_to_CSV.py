#!/usr/bin/python3
'''
Python script that use API,
to export data in the CSV format.
'''
import requests
import sys
import csv

if __name__ == "__main__":
    emp_id = sys.argv[1]
    emp_name = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                            .format(emp_id)).json().get("username")
    sums = 0
    done = []
    x = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    for todos in x:
        if (todos.get("userId") == int(emp_id)):
            tmp = []
            tmp.extend((emp_id,
                        emp_name,
                        todos.get("completed"),
                        todos.get("title")))
            all.append(tmp)

    with open("{}.csv".format(emp_id), 'w+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(all)
