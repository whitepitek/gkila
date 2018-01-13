#!/usr/bin/env python3

import argparse
import pymysql.cursors
import sqlite3
import pprint

SPHINX_IP = '127.0.0.1'
SPHINX_PORT = 10001
PREFIX = '/home/gkila/gkila'
DBPATH = PREFIX + '/magnetico.db'

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', nargs='+')
    parser.add_argument('--relevance', action='store', type=float, default=0.5)
    return parser.parse_args()


def get_file_ids(keywords):
    conn = pymysql.connect(host=SPHINX_IP, port=SPHINX_PORT, charset='utf8')
    with conn.cursor() as cursor:
        query = ('''
            SELECT *
            FROM main
            WHERE MATCH(%s)
            ''', (' '.join(keywords)))
        cursor.execute(*query)
        ids = [fid for fid, in cursor]
    conn.close()
    return ids


def hash_to_str(h):
    return ''.join(['{:02x}'.format(c) for c in h])


def get_path(file_id):
    with sqlite3.connect(DBPATH) as conn:
        conn.text_factory = bytes
        cursor = conn.cursor()
        request = ('''
            SELECT torrents.info_hash, files.path
            FROM files
            INNER JOIN torrents
            ON files.torrent_id = torrents.id
            WHERE files.id = ?
            ''', (str(file_id), ))
        cursor.execute(*request)
        info_hash, path = cursor.fetchone()
        return hash_to_str(info_hash) + '/' + path.decode()


def get_results(keywords):
    res = dict()
    for fid in get_file_ids(keywords):
        res[get_path(fid)] = 1
    return res

def main():
    args = get_args()
    res = get_results(args.keyword)
    pprint.PrettyPrinter().pprint(res)


if __name__ == '__main__':
    main()
