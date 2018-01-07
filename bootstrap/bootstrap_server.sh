#!/bin/bash

projects[0]=golang
projects[1]=walker
projects[2]=client

source common/common.sh

cmd=$1
if [[ "$cmd" != "install" && "$cmd" != "update" ]]; then
    echo "Bad command" >&2
    exit 1
fi

function stop_working() {
    pkill -f "$prefix/common/loop_fg.sh"
    pkill -f magneticod
    searchd --config $prefix/walker/sphinx.conf --stopwait
    pkill -f searchd
    return 0
}

function install() {
    mkdir -p "$prefix/bin"
    for project in ${projects[*]}; do
        if [[ $cmd == "install" ]]; then
            echo "Installing ${project}..." >&2
            "${prefix}/${project}"/install.sh
            if [[ $? != 0 ]]; then
                echo "Installing ${project} FAILED" >&2
                return 1
            fi
            echo "Installing ${project}: done." >&2
        fi
        echo "Updating ${project}..." >&2
        "${prefix}/${project}"/update.sh
        if [[ $? != 0 ]]; then
            echo "Updating ${project} FAILED" >&2
            return 1
        fi
        echo "Updating ${project}: done." >&2
    done
    return 0
}

function run() {
    for project in ${projects[*]}; do
        echo "Running ${project}..." >&2
        "${prefix}/${project}"/run.sh
        if [[ $? != 0 ]]; then
            echo "Running ${project} FAILED" >&2
            return 1
        fi
        echo "Running ${project}: done." >&2
    done
    return 0
}

sure_run stop_working
sure_run install
echo "Installation done." >&2
sure_run run
echo "Running done." >&2
