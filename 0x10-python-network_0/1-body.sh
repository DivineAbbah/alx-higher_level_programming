#!/bin/bash
#  send a GET method request to the URL, and display only body of a 200 status code response
curl -s "$1" -X GET -L
