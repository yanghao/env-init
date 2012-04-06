def do():
    fd = open("package.txt")
    package = fd.readlines()
    fd.close()

    cmd = "apt-get install -y "

    for p in package:
	cmd = cmd + p.strip() + ' '

    from commands import getstatusoutput as getso

    s,o = getso(cmd)

    from handle_error import handle
    handle(s,o)
