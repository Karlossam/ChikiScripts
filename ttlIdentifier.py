#!/usr/bin/python2.7

import subprocess, re, sys


def return_ttl(address):
    proc = subprocess.Popen(["ping -c 1 %s" % address, ""], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    out = out.split()
    out = re.findall(r"\d{1,3}",out[12])
    return out[0]


def os_name(ttl):
    if ttl >= 0 and ttl <= 64:
        return "Linux"
    elif ttl > 64 and ttl <= 128:
        return "Windows"
    else:
        return "Unknown"


if len(sys.argv) != 2:
    print "\n[*] Usage: python " + sys.argv[0] + " <ip_address>\n"
    sys.exit(1)

if __name__ == '__main__':
    addr = sys.argv[1]
    ttl = return_ttl(addr)
    
    try:
        print "\n%s --> %s" % (addr,os_name(int(ttl)))
    except:
        pass
