#!/usr/bin/env python

##
##  DEPENDENCIES
##
##  dpkt
##
##      http://code.google.com/p/dpkt
##      download ... decompress
##      python setup.py install
##
##  dnslib
##
##      https://pypi.python.org/pypi/dnslib
##      download ... decompress
##      python setup.py install
##

if __name__ == '__main__':

    import os
    import socket
    import dpkt
    from dnslib import *

    path = os.path.join(os.getcwd(), 'ethernet.pcap')
    f = open(path)
    pcap = dpkt.pcap.Reader(f)

    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            if eth.type == 2048:
                    ##
                    ## IP Packet
                    ##
                    ip = eth.data
                    ip_src = socket.inet_ntoa(ip.src)
                    ip_dst = socket.inet_ntoa(ip.dst)
                    if ip.p == 17:
                        ##
                        ## UDP
                        ##
                        udp = ip.data
                        if udp.dport == 53 or udp.sport == 53 and len(udp.data) > 0:
                            ##
                            ## DNS request or response
                            ##
                            dns = DNSRecord.parse(udp.data)
                            print '\nDNS Request or Response:(SRC: %s DST: %s)\n%s\n'%(ip_src, ip_dst, dns)
                            

        except Exception, e:
            print e
            pass
