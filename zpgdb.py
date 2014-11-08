# -*- coding: utf-8 -*-

"""This module provides a thin wrapper to access a PostgreSQL database,
with functions to create a connection per thread, context managers to
wrap transactions, etc"""

import psycopg2
import threading

HOST = PORT = DB = USER = PASS = None

_local = threading.local()

def getdb():
    if not hasattr(_local, 'dbh'):
        _local.dbh = psycopg2.connect(host=HOST, port=PORT,
            database=DB, user=USER, password=PASS)
    return _local.dbh
