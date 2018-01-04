#!/bin/bash

# root directory to copy to the remote server FIXME
localroot=$(pwd)
# ssh pubkey FIXME
pubkey=$(cat "$HOME/.ssh/id_rsa.pub")
# ssh host name of the remote server FIXME
host="kila"

rcp="rsync -aqz"

source common/common.sh

# Prepare user
#sure_run ssh root@"$host" useradd -m -s /bin/bash gkila
#sure_run ssh root@"$host" mkdir -p /home/"$user"/.ssh
#sure_run ssh root@"$host" echo "$pubkey" \> /home/"$user"/.ssh/authorized_keys
# Clean up target directory
#sure_run ssh "$user@$host" rm -rf "$prefix"
sure_run $rcp "$localroot/" "$user@$host:$prefix"
# Bootstrap in place
sure_run ssh "$user@$host" "cd \"$prefix\" && ./bootstrap/bootstrap_server.sh"

echo "Deploy finished" >&2
