#!/bin/bash

user="gkila"               # user name for gkila server user
prefix="/home/$user/gkila" # installation prefix

# environment
export GOPATH="$prefix/gobuild"
export PATH="$PATH:$GOPATH/go/bin:$GOPATH/bin/"

function sure_run() {
    "$@"
    local status=$?
    if [[ $status != 0 ]]; then
        echo "command $1 failed with status $status" >&2
        exit 1
    fi
}
