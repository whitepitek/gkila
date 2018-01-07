#!/usr/bin/env python3

import argparse
import sqlite3


PREFIX = '/home/gkila/gkila'
DBPATH = PREFIX + '/magnetico.db'
NEXT_ID_PATH = PREFIX + '/walker/next_id.txt'
ERROR_LOG_PATH = PREFIX + '/walker/get_index_updates_errors.log'


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--all', action='store_true')
    return parser.parse_args()

def get_forms(path):
    return path

def escape(s):
    return ('"' +
            s.translate(str.maketrans({'"': '""'})) +
            '"')



def print_csv(next_id):
    with sqlite3.connect(DBPATH) as conn:
        conn.text_factory = bytes
        cursor = conn.cursor()
        request = ('''
            SELECT files.id, path
            FROM files
            INNER JOIN torrents
            ON files.torrent_id = torrents.id
            WHERE files.id >= ?
            ''', (str(next_id), ))
        for row in cursor.execute(*request):
            last_id = row[0] + 1
            try:
                path = row[1].decode()
            except UnicodeDecodeError:
                with open(ERROR_LOG_PATH, 'at') as log:
                    print('{}: unicode error'.format(last_id), file=log)
                continue
            forms = get_forms(path)
            print('{},{}'.format(last_id, escape(forms)))
            next_id = last_id + 1
    return next_id

def get_next_id():
    try:
        with open(NEXT_ID_PATH, 'rt') as next_id_f:
            return int(next_id_f.read())
    except:
        return 0

def store_next_id(next_id):
    with open(NEXT_ID_PATH, 'wt') as next_id_f:
        print(next_id, end='', file=next_id_f)

def main():
    args = get_args()
    if args.all:
        next_id = 0
    else:
        next_id = get_next_id()
    next_id = print_csv(next_id)
    store_next_id(next_id)

if __name__ == '__main__':
    main()
