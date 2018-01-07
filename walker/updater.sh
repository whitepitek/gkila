#!/bin/bash

source common/common.sh

while true; do
    # about once in an hour
    indexer --config $prefix/walker/sphinx.conf --merge main delta --rotate
    for i in {0..59}; do
        # about once in a minute
        indexer --config $prefix/walker/sphinx.conf delta --rotate
        sleep 60
    done
done
