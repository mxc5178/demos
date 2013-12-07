#!/usr/bin/env python

##
##  DEPENDENCIES
##
##  step
##
##      https://pypi.python.org/pypi/stem/
##      download ... decompress
##      python setup.py install
##
##  socksipy
##      https://code.google.com/p/socksipy-branch/
##

import sys
import socks
import socket
import stem
import stem.process
from stem import Signal
from stem.connection import connect_port
from stem.util import term

def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

def print_bootstrap_lines(line):
    if "Bootstrapped" in line:
        print(term.format(line, term.Color.BLUE))

if __name__ == '__main__':

    tor_process = stem.process.launch_tor_with_config(
        config = {
            'SocksPort':str(9050),
            'ControlPort':str(9051),
        },
        init_msg_handler = print_bootstrap_lines,
        completion_percent = 100,
        timeout = 3600,
        take_ownership = True
    )

    controller = connect_port()

    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket
    socket.create_connection = create_connection
    ##
    ## import the browser class **after** the tor proxy is set
    ##
    import mechanize
    from mechanize import Browser

    ##
    ## loop 20 times, changing exit node each time
    ##      ...there may be a better way to do this
    ##
    for i in range(0,19):

        controller.new_circuit()

        br = Browser()
        print br.open('http://lab46.corning-cc.edu/~mcooper6/myip/').read()

        controller.signal(Signal.NEWNYM)

    controller.close()
    tor_process.kill()
