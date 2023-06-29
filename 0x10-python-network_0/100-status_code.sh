#!/bin/bash
# pass an argument, display status code of the response
curl -sI -w '%{response_code}' "$1" -o /dev/null
