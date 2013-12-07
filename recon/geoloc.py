#!/usr/bin/env python

##
##  DEPENDENCIES
##
##  pygeoip
##
##      http://code.google.com/p/pygeoip
##      https://github.com/appliedsec/pygeoip
##      easy_install pygeoip
##
##  maxmind GeoLiteCity
##      http://www.maxmind.com/app/geolitecity
##      download ... decompress
##      place in the data directory
##

if __name__ == '__main__':

    import os
    import pygeoip

    geopath = os.path.join(os.getcwd(), 'data', 'geo-city.dat')
    gi = pygeoip.GeoIP(geopath)

    ippath = os.path.join(os.getcwd(), 'data', 'ipaddrs.txt')
    with open(ippath, 'r') as f:
        for ip in f:
            try:
                rec = gi.record_by_name(ip.strip())
                lat = rec['latitude']
                lon = rec['longitude']
                ##
                ## <ip>:<lat>:<lon>
                ##
                print '%s:%s:%s'%(ip.strip(), lat, lon)
            except Exception, e:
                pass

