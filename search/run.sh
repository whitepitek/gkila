#!/bin/bash

source common/common.sh

loop searchd --config $prefix/search/sphinx.conf --nodetach --pidfile
