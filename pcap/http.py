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

                    if ip.p == 6:
                        ##
                        ## TCP
                        ##
                        ip_src = socket.inet_ntoa(ip.src)
                        ip_dst = socket.inet_ntoa(ip.dst)
                        tcp = ip.data
                        if tcp.dport in[8080,80] and len(tcp.data) > 0:
                            ##
                            ## HTTP traffic
                            ##
                            try:
                                http = dpkt.http.Request(tcp.data)
                                ##
                                ## <src ip>:<dst ip>:<requested host>:<requested uri>
                                ##
                                print '%s:%s:%s%s'%(ip_src, ip_dst, str(http.headers['host']), str(http.uri))

                            except Exception, e:
                                pass

        except Exception, e:
            pass
