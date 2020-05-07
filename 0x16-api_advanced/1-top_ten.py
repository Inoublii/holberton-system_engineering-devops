#!/usr/bin/python3
"""
top_ten
"""

import requests


def top_ten(subreddit):
    """
    titles of the 10 hot posts
    """
    if subreddit is None or type(subreddit) is not str:
        print(None)

    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Python/requests:api.advanced:v1.0.0 (by /u/aleix)'}
    params = {'limit': 10}
    requ = requests.get(url, headers=headers, params=params).json()
    posts = requ.get('data', {}).get('children', None)
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        print(None)
    else:
        for post in posts:
            print(post.get('data', {}).get('title', None))
