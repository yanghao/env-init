PBASE = "package"

def do():
    fd = open("package.txt")
    files = fd.readlines()
    fd.close()

    cmd = "apt-get install -y "

    for p in files:
        p = p.strip()
        if p:
            fd = open(PBASE + '/' + p)
            packages = fd.readlines()
            fd.close()
            for package in packages:
                    cmd = cmd + package.strip() + ' '
        else:
            continue

    from commands import getstatusoutput as getso

    s,o = getso(cmd)

    from handle_error import handle
    handle(s,o)
