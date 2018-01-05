#!/bin/bash

source common/common.sh

loop magneticod --database=sqlite3://$prefix/magnetico.db -v
