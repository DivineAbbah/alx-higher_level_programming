#!/bin/bash
# Send a JSON POST and displays body of the response
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
