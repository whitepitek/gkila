#!/bin/bash

source common/common.sh

loop magneticod --database=sqlite3://$prefix/magnetico.db -v
loop updater
loop searchd --config $prefix/walker/sphinx.conf --nodetach --pidfile
