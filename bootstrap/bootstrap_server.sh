#!/bin/bash

projects[0]=golang
projects[1]=walker
projects[2]=client
projects[3]=search

source common/common.sh

function stop_working() {
    pkill -f "$prefix/common/loop_fg.sh"
    pkill -f magneticod
    pkill -f searchd
    return 0
}

function install() {
    mkdir -p "$prefix/bin"
    for project in ${projects[*]}; do
        echo "Installing ${project}..." >&2
        "${prefix}/${project}"/install.sh
        if [[ $? != 0 ]]; then
            echo "Installing ${project} FAILED" >&2
            return 1
        fi
        echo "Installing ${project}: done." >&2
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
