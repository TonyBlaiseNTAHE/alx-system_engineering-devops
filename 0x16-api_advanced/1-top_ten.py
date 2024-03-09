#!/usr/bin/python3

"""
0-subs module
"""
import requests


def top_ten(subreddit):
    """ returns the number of subscribes from reddit api"""
    if subreddit is None or type(subreddit):
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"limit": 10}
    response = requests.get(url=url, headers=header, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return 0
    data = response.json().get("data")
    for title in data.get("children"):
        print(title.get('data').get('title'))
