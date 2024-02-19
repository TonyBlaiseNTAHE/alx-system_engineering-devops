#!/usr/bin/python3

"""
a script that take an id of an user and return to list of tasks
that he/she already done or not yet done using REST API
"""

import requests
import sys


if __name__ == '__main__':
    url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    res = requests.get(url)
    j_res = res.json()
    name = j_res.get('username')
    print(name)
