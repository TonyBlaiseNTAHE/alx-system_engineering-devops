#!/usr/bin/python3

"""
a script that take an id of an user and return to list of tasks
that he/she already done or not yet done using REST API
"""
import csv
import requests
import sys



if __name__ == '__main__':
    user_id = sys.argv[1]
    """ fetching username"""
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    res = requests.get(url)
    j_res = res.json()
    name = j_res.get('username')

    """ fetch all tasks for the user"""
    todos = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    result = requests.get(todos)
    user_todos = result.json()
    all_tasks = []
    for task in user_todos:
        all_tasks.append([user_id,
                          name,
                          task.get('completed'),
                          task.get('title')])

    filename = f'{user_id}.cvs'
    with open(filename, 'w', newline='') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=",",
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in all_tasks:
            employee_writer.writerow(task)
