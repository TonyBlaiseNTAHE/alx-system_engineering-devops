#!/usr/bin/python3

"""
0-subs module
"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribes from reddit api"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {
        "User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr"
    }
    response = requests.get(url=url, headers=header, allow_redirects=False)
    if response.status_code == 404:
        return 0
    data = response.json().get("data")
    return data.get("subscribers")