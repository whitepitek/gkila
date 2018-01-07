#!/bin/bash

source common/common.sh

set -e

sure_run go get github.com/anacrolix/torrent/cmd/torrent-pick
sure_run go install github.com/anacrolix/torrent/cmd/torrent-pick
