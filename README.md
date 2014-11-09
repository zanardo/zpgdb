# zpgdb - Python library for simple PostgreSQL connection and transaction management

`zpgdb` is a small library to ease the management of PostgreSQL database
connection between your app modules and packages, and provides a simple context
manager to wrap code that should run database commands inside a transaction,
with automatic commit or rollback.

Database connections are reused and one connection is opened by thread. Only
one connection type is permitted at this time (eg, the same host, port, user and
password and database).

## How to use

	# You can import the module on every package/module you want to share
	# the database connection.
	import zpgdb as db

	# The access configuration needs to be done only one time, preferably
	# inside your __main__ block.
	db.config_connection(host, port, user, password, database)

	# You can get the connection object directly. `getdb()` will start a
	# new connection if there is no connection opened with the actual thread.
	dbh = db.getdb()

	# Or you can start a context manager getting a cursor, with automatic
	# commit on finish, or rollback in case there is a exception thrown.
	with db.trans() as c:
		c.execute('...')
		c.execute('...')
		for row in c:
			...