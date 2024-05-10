#!/bin/bash
# Display size of body of response; Usage: ./0-body_size.sh 0.0.0.0:5000
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '

# there is another method easier using wc -c to count the response content words but we are studing network and http requests
