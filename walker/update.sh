#!/bin/bash

source common/common.sh

set -e

sure_run cp "$prefix/walker/get_index_updates.py" "$prefix/bin/get_index_updates"
sure_run cp "$prefix/walker/updater.sh" "$prefix/bin/updater"
sed -i "s|__PREFIX__|${prefix}|g" "$prefix/walker/sphinx.conf"
