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
    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
        


def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['id'], post['title'], post['body'])

        with open(posts.csv, 'w', encoding='utf-8') as f:
            fieldname = ['id', 'title', 'body']
            write = csv.DictWriter(f, fieldnames=fieldname)
            write.writeheader()
            for post in posts:
                write.writerow({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                })
fetch_and_print_posts()
fetch_and_save_posts()