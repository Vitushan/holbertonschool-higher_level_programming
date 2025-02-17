#!/usr/bin/python3
"""
create a script for getting posts since an API service
and manipulate this data by help of Python
"""


import requests
import csv


def fetch_and_print_posts():
    """
    Fetch and print posts from the API.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])




def fetch_and_save_posts():
    """
    Fetch and save all posts from
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])

            writer.writeheader()

            for post in posts:
                writer.writerow({"id": post["id"], "title": post["title"], "body": post["body"]})
        print("Data saved to 'posts.csv'.")
    else:
        print("Failed to fetch posts. Status code: {}".format(response.status_code))
