#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user = '{}users/{}'.format(url, userid)
    res = requests.get(user)
    json_o = res.json()
    name = json_o.get('username')

    todos = '{}todos?userId={}'.format(url, userid)
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        t = {"task": task.get('title'),
             "completed": task.get('completed'),
             "useername": name}
        l_task.append(t)

    d = {str(userid): l_task}
    filename = '{}.json'.format(userid)
    with open(filename, mode='w') as file:
        json.dump(d, file)
