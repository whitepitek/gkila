#!/bin/bash

#projects[0]=golang
#projects[1]=walker

source common/common.sh

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

sure_run install
echo "Installation done." >&2
