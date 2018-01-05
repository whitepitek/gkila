# Gkila

## Components
### Index
command: `add_word <hash> <word>`

Add a keyword <word> corresponding to <hash> to the "new" index
return 0 on success, 1 on failure

command: `update_index`

Update the "stable" index merging in with the "new" one.
return 0 on success, 1 on failure
### Walker
Walk through DHT, find torrents, add them to index.
command: `walker`

This is a wrapper script which runs magneticod and builds a database with the
table "files" with the following scheme: `uint64 id, char[40] hash, char[] path`

command: `get_index_updates [--all]`

Print new items in csv:

    "id","name forms\, space separated"
    "id","name forms\, space separated"
    ...

If `--all` specified, print all the items; otherwise print only new ones since
the last run.
### Search
command: `search [--relevance <relevance>] <keyword> [keyword [...]]`

Search for specified keywords in the "stable" index. Print json file to
stdout. Output format is as follows:

    {
        "path1": relevance (float from (0, 1]),
        "path2": relevance,
        ...
    }

with the highest relevance first, minimum relevance can be specified in
the command. Path shell have the following format:
"hash/path_to_file", where path_to_file is a relevant path to the file
inside torrent.

return 0 on success, 1 on failure
### Head server
Head server will handle clients' requests and respond with results from
search command. Basically, it will be simple HTTP server with usage
as follows:

    server <ip>:<port>

Requests format (json):

    {
        keywords: [ "word1", "word2", ...]
    }

Requests will be extended in future.
The response will be like the output of the `search` command:

    {
        results: [
            "path1": relevance (int),
            "path2": relevance,
            ...
            ]
    }

with the highest relevance first.
Again, responses probably will be extended in future.
### Client
1. Client library.
The library shell encapsulate the following functions:
* Given search request, return the list of paths (through request to a
        head server)
* Translate the path to a magnet link
* Download specified path
1. Command line client.
Implement command line interface to the library<br>
command: `gkila search <word1> [word2 [...]]`<br>
Search for specified keywords and print the results<br>
command: `gkila magnet <path>`<br>
Translate path to a magnet link<br>
command: `gkila download <path> <save_path>`<br>
Download file specified in "path" (which is actually "hash/path_to_file")
and save it to "save_path"
1. QT client
Implement pretty gui with the same features as command line client has.
### Management scripts
Bootstrap, run, keep running.
