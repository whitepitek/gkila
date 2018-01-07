#!/bin/bash

source common/common.sh

set -e

mkdir -p "$prefix/gobuild"
cd "$prefix/gobuild"
wget -q https://redirector.gvt1.com/edgedl/go/go1.9.2.linux-amd64.tar.gz
tar -xf go1.9.2.linux-amd64.tar.gz
go get -u github.com/golang/dep/cmd/dep
cd "$prefix"
