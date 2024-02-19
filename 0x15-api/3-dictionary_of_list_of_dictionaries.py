#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = f'{url}users'
    response = requests.get(user)
    res_json = response.json()
    d_task = {}
    for user in res_json:
        name = user.get('username')
        user_id = user.get('id')
        todos = f'{url}todos?userId={user_id}'
        res = requests.get(todos)
        tasks = res.json()
        all_tasks = []
        for task in tasks:
            dict_task = {"username": name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            all_tasks.append(dict_task)

        d_task[str(user_id)] = all_tasks
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as file:
        json.dump(d_task, file)
