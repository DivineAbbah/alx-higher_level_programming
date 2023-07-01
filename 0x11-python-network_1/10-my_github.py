#!/usr/bin/python3
"""A script to take  GitHub credentials (username and password) as arguments
and uses the GitHub API to display users id"""

if __name__ == '__main__':
    import sys
    from requests import get
    from requests.auth import HTTPBasicAuth

    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
