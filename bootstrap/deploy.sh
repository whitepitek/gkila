#!/bin/bash

# root directory to copy to the remote server FIXME
localroot=$(pwd)
# ssh pubkey FIXME
pubkey=$(cat "$HOME/.ssh/id_rsa.pub")
# ssh host name of the remote server FIXME
host="kila"

rcp="rsync -aqz"

source common/common.sh

function install() {
    # Install packages
    sure_run ssh root@"$host" apt install mysql-client libmysqlclient20 unixodbc libpq5 -y
    sure_run ssh root@"$host" wget -q http://sphinxsearch.com/files/sphinxsearch_2.3.2-beta-1~xenial_amd64.deb
    sure_run ssh root@"$host" dpkg -i sphinxsearch_2.3.2-beta-1~xenial_amd64.deb
    sure_run ssh root@"$host" rm sphinxsearch_2.3.2-beta-1~xenial_amd64.deb

    # Prepare user
    sure_run ssh root@"$host" useradd -m -s /bin/bash gkila
    sure_run ssh root@"$host" mkdir -p /home/"$user"/.ssh
    sure_run ssh root@"$host" echo "$pubkey" \> /home/"$user"/.ssh/authorized_keys

    # Clean up target directory
    sure_run ssh "$user@$host" rm -rf "$prefix"

    sure_run $rcp "$localroot/" "$user@$host:$prefix"
    # Bootstrap in place
    sure_run ssh "$user@$host" "cd \"$prefix\" && ./bootstrap/bootstrap_server.sh install"
}

function update() {
    sure_run $rcp "$localroot/" "$user@$host:$prefix"
    # Bootstrap in place
    sure_run ssh "$user@$host" "cd \"$prefix\" && ./bootstrap/bootstrap_server.sh update"
}

if [[ "$1" == "install" ]]; then
    install
elif [[ "$1" == "update" ]]; then
    update
else
    echo "Bad command" >&2
    exit 1
fi

echo "Deploy finished" >&2
