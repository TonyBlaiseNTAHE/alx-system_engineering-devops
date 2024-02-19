#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user = f'{url}users/{userid}'
    response = requests.get(user)
    resp_json = response.json()
    name = resp_json.get('username')

    todos = f'{url}todos?userId={userid}'
    response2 = requests.get(todos)
    tasks = response2.json()
    all_task = []
    for task in tasks:
        dict_task = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": name}
        all_task.append(dict_task)

    d_task = {str(userid): all_task}
    filename = '{}.json'.format(userid)
    with open(filename, mode='w') as f:
        json.dump(d_task, f)
