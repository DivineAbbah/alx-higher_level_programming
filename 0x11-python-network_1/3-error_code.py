#!/usr/bin/python3
"""A script to take in a URL,
sends a req to the URL and displays
the body of the response (decoded in utf-8)."""

if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    import sys

    url = Request(sys.argv[1])
    try:
        with urlopen(url) as res:
            url_res = res.read()
            print(url_res.decode('utf-8'))

    except HTTPError as err:
        print("Error code: {}".format(err.code))
