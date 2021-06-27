#!/bin/bash

awk -F'"' '$0 ~ /selenoid/ {print $4}' etc/selenoid/browsers.json | while read line; do docker pull "$line"; done
