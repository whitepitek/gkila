#!/bin/bash

source common/common.sh

set -e

sed -i "s|__PREFIX__|${prefix}|g" "$prefix/search/sphinx.conf"
