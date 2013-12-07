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

if __name__ == '__main__':

    import os
    import socket
    import dpkt

    path = os.path.join(os.getcwd(), 'ethernet.pcap')
    try:
        with open(path, 'r') as f:
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

                        ##
                        ## <frag ID>:<src IP>:<dst IP>
                        ##
                        print '%s:%s:%s'%(ip.id, ip_src, ip_dst) 

                except Exception, e:
                    pass

    except Exception, e:
        pass
