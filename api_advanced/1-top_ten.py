#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'my-reddit-bot/0.1 by YOUR_USERNAME'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data', {})
    posts = data.get('children', [])

    if not posts:
        print(None)
        return

    for post in posts:
        print(post['data'].get('title', 'No title found'))

