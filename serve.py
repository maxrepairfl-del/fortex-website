#!/usr/bin/env python3
"""Minimal static file server for local preview of dist/.

Avoids `python -m http.server`, whose argparse evaluates os.getcwd() at import
(which can fail under a restricted launch cwd). We chdir to an absolute dist
path and bind the handler to it explicitly.
"""
import functools
import http.server
import os
import socketserver
import sys

DIST = "/Users/max/Desktop/operations/website/dist"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8092

os.chdir(DIST)
Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIST)


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


with Server(("127.0.0.1", PORT), Handler) as httpd:
    print(f"Serving {DIST} at http://127.0.0.1:{PORT}")
    httpd.serve_forever()
