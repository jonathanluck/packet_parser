#!/bin/bash

sudo python3 server.py &> /dev/null &
firefox index.html
sudo fuser -k 80/tcp

