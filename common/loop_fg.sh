#!/bin/bash

while true; do
    echo "Running $@"
    "$@"
    echo "$@ exited with code $?"
    sleep 0.1
done
