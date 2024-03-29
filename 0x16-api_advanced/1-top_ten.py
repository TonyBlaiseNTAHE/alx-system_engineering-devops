#!/usr/bin/python3

"""
0-subs module
"""
import requests


def top_ten(subreddit):
    """Prints the titles of top 10 hot posts from the specified subreddit."""
    if subreddit is None:
        return 0
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"limit": 10}
    response = requests.get(url=url, headers=header, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return
    data = response.json().get("data")
    for title in data.get("children"):
        print(title.get('data').get('title'))
