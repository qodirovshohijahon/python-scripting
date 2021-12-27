#!/usr/bin/env python

from fabric import Connection

result = Connection('70.34.211.126').run('uname -s', hide=True)
msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
print(msg.format(result))
