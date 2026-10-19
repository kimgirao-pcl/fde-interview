"""
Debug Exercise: Data Pipeline Theme (Standard)

This script should fetch a list of posts for a given user id, fetch that user's
profile, join them together, and print a small report: the user's name, how
many posts they have, and the average title length. It does not currently run
correctly. Find and fix the bugs and supply the missing pieces.

Intended usage:
    python api_test.py 3
"""

import argparse
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument("user_id")
args = parser.parse_args()

base = "https://jsonplaceholder.typicode.com"
posts_url = base + "/posts?userId=" + args.user_id

def fetch_data():
    global posts, user
    posts = requests.get(posts_url).json()
    user = requests.get(user_url).json()

def report_name(user):
    print("User:", user["name"])

def report_post_count(posts):
    print("Number of posts:", len(data))

def report_avg_title_len(posts):
    pass

if __name__ == '__main__':
    fetch_data()
    report_name(user)
    report_post_count(posts)
    report_avg_title_len(posts)