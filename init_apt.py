def do():
    fd = open('/etc/apt/apt.conf','w')
    fd.write('Acquire::http::proxy "http://proxy-prc.intel.com:911";')
    fd.close()

#   from commands import getstatusoutput as getso
#   from handle_error import handle

#   s,o = getso("apt-get update")

#   handle(s,o)

#   s,o = getso("apt-get upgrade -y")

#   handle(s,o)
