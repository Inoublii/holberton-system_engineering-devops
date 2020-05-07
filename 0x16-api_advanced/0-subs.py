#!/usr/bin/python3
"""
number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    number of subscribers
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'Python/requests:api.advanced:v1.0.0 (by /u/aleix)'}
    requ = requests.get(url, headers=headers).json()
    subs = requ.get("data", {}).get("subscribers", 0)
    return subs
