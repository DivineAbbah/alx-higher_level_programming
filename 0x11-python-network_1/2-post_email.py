#!/usr/bin/python3
"""A script to take in a URL and an email,
sends a POST req to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    import sys

    url_ = sys.argv[1]
    mail = {'email': sys.argv[2]}
    email = urlencode(mail)
    email = email.encode('ascii')
    url_req = Request(url_, email)

    with urlopen(url_req) as res:
        url_res = res.read()
    output = url_res.decode('utf-8')
    print(output)
