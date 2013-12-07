#!/usr/bin/env python

##
##  DEPENDENCIES
##
##  pywhois
##
##      https://code.google.com/p/pywhois/
##      download ... decompress
##      python setup.py install
##

if __name__ == '__main__':

    import os
    import PyWhois

    path = os.path.join(os.getcwd(), 'data', 'hosts.txt')
    with open(path, 'r') as f:
        for line in f:
            
            try:
                w = PyWhois.whois(line.strip())
                str(w)
                for a in dir(w):
                    if not a.startswith('__') and not callable(getattr(w,a)):

                        if a == 'emails' and len(w.emails) > 0:
                            print 'EMAILS: %s'%w.emails

                        elif a == 'registrant_name' and len(w.registrant_name) > 0:
                            print 'REGISTRANT: %s'%w.registrant_name
     
                        elif a == 'name_servers' and len(w.name_servers) > 0:
                            print 'NAME SERVERS: %s'%w.name_servers

            except Exception, e:
                pass

