#!/usr/bin/python3

"""
a script that take an id of an user and return to list of tasks
that he/she already done or not yet done using REST API
"""

import requests
from sys import argv


def fetch_todos():
    """ fetching all todos list """
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(todos_url)
    if response.status_code == 200:
        todos = response.json()
        return todos
    else:
        print(f"Failed to fetch todos. Status code: {response.status_code}")
        return []


def organize_todo_by_user(todos, user_id):
    """
    this methods is for getting a list of
    all the tasks that a user has.
    """
    user_todos = []
    for todo in todos:
        if todo['userId'] == int(user_id):
            user_todos.append(todo)
    return user_todos


def fetch_user_name(user_id):
    """
    fetch the user name
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(user_url)
    if response.status_code == 200:
        user_data = response.json()
        return user_data['name']
    else:
        print(f"Failed to fetch user")
        return None


if __name__ == '__main__':
    """ step1: get/fetch all todo lists """
    user_name = ""
    count = 0
    total_task = 0
    user_id = argv[1]
    todos = fetch_todos()
    user_name = fetch_user_name(user_id)
    if todos:
        user_todos = organize_todo_by_user(todos, user_id)
        if user_todos:
            for todo in user_todos:
                if todo['completed']:
                    count += 1
                total_task += 1
            print(
                  f"Employee {user_name} is done with "
                  f"tasks({str(count)}/{str(total_task)})"
                )
            for todo in user_todos:
                if todo['completed']:
                    print(f"\t{todo['title']}")
        else:
            print(f"No tasks found for user {user_id}.")
    else:
        print("No todos fetched.")
