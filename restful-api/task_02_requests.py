#!/usr/bin/python3
"""
task_02_requests.py
Consume and process data from JSONPlaceholder using requests.
"""

import csv
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print:
    - Status Code: <code>
    - Titles of all posts (one per line) if successful
    """
    try:
        response = requests.get(API_URL, timeout=10)
    except requests.RequestException:
        # If the request fails (network/DNS/timeout), we still follow the format
        print("Status Code: None")
        return

    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        return

    try:
        posts = response.json()
    except ValueError:
        # Invalid JSON
        return

    for post in posts:
        title = post.get("title", "")
        print(title)


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder and save to posts.csv.
    Only saves if request is successful (HTTP 200) and JSON is valid.

    CSV columns: id, title, body
    """
    try:
        response = requests.get(API_URL, timeout=10)
    except requests.RequestException:
        return

    if response.status_code != 200:
        return

    try:
        posts = response.json()
    except ValueError:
        return

    # Build list of dictionaries with only the required keys
    data = [
        {
            "id": post.get("id"),
            "title": post.get("title", ""),
            "body": post.get("body", ""),
        }
        for post in posts
    ]

    fieldnames = ["id", "title", "body"]

    with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
