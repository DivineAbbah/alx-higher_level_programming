#!/usr/bin/python3
"""A script that sends  request to a URL that displays the body of the response."""

if __name__ == "__main__":
    import sys
    import requests

    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
