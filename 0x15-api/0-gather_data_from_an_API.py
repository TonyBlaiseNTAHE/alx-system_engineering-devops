#!/usr/bin/python3

"""
a script that take an id of an user and return to list of tasks
that he/she already done or not yet done using REST API
"""

import requests
import sys


if __name__ == '__main__':
    user = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    response = requests.get(user)
    j_resp = response.json()
    print("Employee {} is done with ".format(j_resp.get('name')), end="")
    todos = f'https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}'
    result = requests.get(todos)
    user_todos = result.json()
    done_task = []
    for task in user_todos:
        if task.get('completed') is True:
            done_task.append(task)
    print("({}/{})".format(len(done_task), len(user_todos)))
    for task in done_task:
        print("\t{}".format(task.get('title')))
