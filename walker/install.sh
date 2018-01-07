#!/bin/bash

source common/common.sh

set -e

function install_magneticod() {
    git clone https://github.com/boramalper/magnetico.git "$GOPATH/src/magnetico"
    cd "$GOPATH/src/magnetico"
    git checkout go-rewrite
    dep ensure
    # FIXME Patches. That's probably the worst way to apply it.
    printf "func NewDecoder2(r interface {io.ByteScanner; io.Reader}) *Decoder {\n    return &Decoder{r: r}\n}" >> $GOPATH/src/magnetico/vendor/github.com/anacrolix/torrent/bencode/api.go
    sed -i 's/DROP INDEX/DROP INDEX IF EXISTS/g' persistence/sqlite3.go
    go install magnetico/magneticod
    cp "$GOPATH/bin/magneticod" "$prefix/bin/"
    cd $prefix"
}

sure_run install_magneticod
