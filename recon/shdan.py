#!/usr/bin/env python

##
##  DEPENDENCIES
##
##  shodan
##
##      https://pypi.python.org/pypi/shodan
##      download ... extract
##      python setup.py install
##

if __name__ == '__main__':

    import os
    import re
    from shodan import WebAPI
    SHODAN_API_KEY = "API-KEY-HERE"
    api = WebAPI(SHODAN_API_KEY)

    info = {}
    path = os.path.join(os.getcwd(), 'data', 'hosts.txt')
    with open(path, 'r') as f:
        for line in f:
            l = line.strip()
            results = api.search(l)
            for r in results['matches']:
                for m in r['data'].split('\n'):
                    match = re.match('^Server: (.*)$', m)
                    if match:
                        ##
                        ## <ip>:<server striing>
                        ##
                        print '%s:%s'%(r['ip'], match.group(1))

