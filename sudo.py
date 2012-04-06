#!/usr/bin/python
import sys
from handle_error import CommandException

do_list = [
    'init_package',
]

n = 0
for item in do_list:
    sys.stdout.write("Running %s ... " % item)
    sys.stdout.flush()
    exec ("%s = __import__('%s')" % (item, item))
    try:
        exec ("%s.do()" % item)
    except CommandException as e:
        fd = open('.step', 'w')
        fd.write('%d %s' % (n, item))
        fd.close()
        print("status: %d", e.status)
        print("output: %s", e.output)
        sys.exit(-1)
    sys.stdout.write("Done.\n")
    sys.stdout.flush()
    n = n + 1

print("Job finished.\n")
