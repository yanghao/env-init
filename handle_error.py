class CommandException(Exception):
    def __init__(self, s, o):
        Exception.__init__(self)
        self.status = s
        self.output = o

def handle(s,o):
    if (s != 0):
	raise CommandException(s,o)
    else:
        return
