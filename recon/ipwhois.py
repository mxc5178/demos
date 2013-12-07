#!/usr/bin/env python

##
## Team Cymru ASN lookup
##

if __name__ == '__main__':

    import os
    import subprocess

    ##
    ## Effectively run the command:
    ##
    ##  netcat whois.cymru.com 43 < list01 | sort -n > list02 
    ##

    cmd = [
        'ncat', 
        'whois.cymru.com', 
        '43'
    ]

    path = os.path.join(os.getcwd(), 'data', 'ipaddrs.txt')
    with open(path, 'r') as f:
        input = f.read()
        pipe = subprocess.Popen(
            cmd, 
            shell=False, 
            cwd=None,
            stdout = subprocess.PIPE,
            stdin = subprocess.PIPE,
            stderr = subprocess.PIPE
        )

        (out, error) = pipe.communicate(input)

        print out
