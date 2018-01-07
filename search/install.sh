#!/bin/bash

source common/common.sh

set -e

mkdir -p $prefix/sphinx_binlog
sed -i "s|__PREFIX__|${prefix}|g" "$prefix/search/sphinx.conf"

sure_run indexer --config "$prefix/search/sphinx.conf" --all
