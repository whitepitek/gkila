#!/bin/bash

while true; do
    # about once in an hour
    indexer --config $prefix/search/sphinx.conf --merge main delta --rotate
    for i in {0..60}; do
        # about once in a minute
        indexer --config $prefix/search/sphinx.conf delta --rotate
        sleep 60
    done
done
