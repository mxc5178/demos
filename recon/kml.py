#!/usr/bin/env python


if __name__ == '__main__':

    import os

    header = '''<?xml version='1.0' encoding='UTF-8'?>
    <kml xmlns='http://earth.google.com/kml/2.0'>
    <Folder><name>Recon Demo KML Output</name>'''

    footer = '''</Folder></kml>'''

    geopath = os.path.join(os.getcwd(), 'data', 'geolocation.txt')

    with open(os.path.join(os.getcwd(), 'ReconDemo.kml'), 'wt') as f:
        f.write(header)
        with open(geopath, 'r') as g:
            for line in g:
                l = line.split(':')
                ip = l[0].strip()
                lat = l[1].strip()
                lon = l[2].strip()

                cdata = """
            <![CDATA[
                IP: %s<br>
                <b>GPS Coordinates</b><br>
                Avg lat/lon: %s, %s
            ]]>""" %(ip, lat, lon)

                fullstr = """
    <Placemark>
        <name>%s</name>
        <description>%s</description>
        <visibility>1</visibility>
        <open>0</open>

        <LookAt>
            <longitude>%s</longitude>
            <latitude>%s</latitude>
            <range>100</range>
            <tilt>54</tilt>
            <heading>-35</heading>
        </LookAt>

        <Point>
            <altitudeMode>clampedToGround</altitudeMode>
            <extrude>0</extrude>
            <tessellate>0</tessellate>
            <coordinates>%s,%s,0</coordinates>
        </Point>
    </Placemark>\n"""%(ip,cdata,lon,lat,lon,lat)

                f.write(fullstr)

        f.write(footer)

