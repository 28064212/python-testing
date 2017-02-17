#! /usr/bin/env python
import sys
import requests

def main():
    print('Hello from Python', sys.version)
    r = requests.get('https://api.github.com/repos/28064212/python-testing')
    print('git name:', r.json()['full_name'])
    print('last update:', r.json()['pushed_at'])

if __name__ == '__main__':
    main()
