#!/usr/bin/env python3
# Code to generate a taginfo project json from an osm2pgsql .style file
import csv
import json

class tag_usage():
    def __init__(self, key, node, way, area):
        self.key = key
        self.node = node
        self.way = way
        self.area = area


taginfo = {
    "data_format": "1",
    "project": {
        "name": "osm2pgsql defaults",
        "description": "Default osm2pgsql C transforms",
        "project_url": "https://github.com/openstreetmap/osm2pgsql",
        "contact_name": "Paul Norman",
        "contact_email": "penorman@mac.com"
    },
    "tags": []
}
with open('default.style', 'r') as style:
    for line in style:
        if line[0] == '#':
            continue
        keyline = line.split()
        if len(keyline) != 4:
            continue
        if keyline[3] == 'delete' or 'nocolumn' in keyline[3]:
            continue
        key = keyline[1]
        object_types = []
        if 'node' in keyline[0]:
            object_types.append('node')
        if 'way' in keyline[0]:
            object_types.append('way')
            if 'polygon' in keyline[3]:
                object_types.append('area')
        taginfo["tags"].append(
            {
                "key": key,
                "object_types": object_types
            })

print(json.dumps(taginfo, indent=4))