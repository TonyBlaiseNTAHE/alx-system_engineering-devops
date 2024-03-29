#!/usr/bin/python3

"""
0-subs module
"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribes from reddit api"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url=url, headers=header, allow_redirects=False)
    if response.status_code == 404:
        return 0
    data = response.json().get("data")
    return data.get("subscribers")
