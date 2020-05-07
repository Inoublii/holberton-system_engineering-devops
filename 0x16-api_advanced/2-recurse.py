#!/usr/bin/python3
"""
recurse
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    all hot post titles
    """
    if subreddit is None or type(subreddit) is not str:
        return None
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Python/requests:api.advanced:v1.0.0 (by /u/aleix)'}
    params = {"after": after, "limit": 100}
    requ = requests.get(url, headers=headers, params=params).json()
    after = requ.get('data', {}).get('after', None)
    posts = requ.get('data', {}).get('children', None)
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        for post in posts:
            hot_list.append(post.get('data', {}).get('title', None))
    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
