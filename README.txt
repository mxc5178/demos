pcap tricks + recon

These are some pcap tricks that I have learned.  These are only a scraching of 
the surface.  The rabbit hole goes deeper than this ... much, much deeper.  So, 
clear your schedule, throw on a pot of cofee and get comfortable.

These demos require:

    python 2.7.3
    dpkt: http://code.google.com/p/dpkt
    BeautifulSoup: http://www.crummy.com/software/BeautifulSoup/
    pywhois: https://code.google.com/p/pywhois/
    pygeoip: https://github.com/appliedsec/pygeoip
    dnslib: https://pypi.python.org/pypi/dnslib
    Maxmind GeoLiteCity.dat: http://www.maxmind.com/app/geolitecity
    shodan: https://pypi.python.org/pypi/shodan
    shodan API key: shodanhq.com


Begin: capture some ethernet/ip traffic and name it ethernet.pcap.  Put it in 
the same folder as parse_eth.py.  Run:

    ./parse_eth.py

You should be able to take this output and arrange it into a list of unique IP 
addresses (if not, there's an example list of IPs) ... name it ipaddrs.txt  
Once you have said list of unique IP addresses, run:

    ./ipwhois.py

This will return a list of ASN numbers, listing the owners of the IP netblocks 
in your pcap.  Next, run:

    ./geoloc.py

This will return a list of latitude/longitude coordinates.  This geolocation is 
as accurate as the free Maxmind GeoLite database ... so your mileage may vary.  
From this output create a colon separated list containing IP:LAT:LON ... name 
it geolocation.txt.  Run:

    ./kml.py

This makes a nifty KML file for Google Earth running.  Open it!

Back to the packet capture ... run:

    ./http.py

Assuming that your traffic capture contains HTTP traffic (not HTTPS), you 
should see a list of URLS that were requested.  Next, run:

    ./dns.py

Assuming that your traffic capture contains DNS traffic, you should now see a 
list of DNS reqests and responses, along with the IP of the source and 
destination.  Use your foo to extract a list of unique hosts ... name it 
hosts.txt.  Now run:

    ./hostwhois.py

A list of registrant names, email addresses and name servers will fly by as you 
watch.  Yippie!  More fodder.  Now run:

    ./shdan.py

This is going to make a call to shodanhq.com using their web API.  You will 
need an API key for this.  At time of writing the cost for a key was $20 USD.  
Pretty reasonable IMHO.  Assuming you have your key, you should now see a list 
of IPs and the servers they are running.  Extract a unique list of servers in 
the form of IP:SERVER and write to a file servers.txt.  Good!  Now run:

    ./exploitdb.py

This will reach out to exploit-db.com and return the results of the server 
string search.

BONUS:

Tor demo that illustrates the use of Tor in python.  You might want to 
reconfigure some of these scripts to use it.  Requires:

    stem: https://pypi.python.org/pypi/stem/
    socksipy: https://code.google.com/p/socksipy-branch/

Run:

    ./tordemo.py
