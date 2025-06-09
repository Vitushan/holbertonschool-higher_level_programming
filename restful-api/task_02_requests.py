#!/usr/bin/python3
"""
this is a module for interpreting python3
"""



import requests, csv

def fetch_and_print_posts():
    """
    fetches all post from JSONPlaceholder.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
