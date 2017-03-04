import json
import re
import geopy
import os

API_KEY = os.environ["GOOGLE_API_KEY"]
geocoder = geopy.GoogleV3(api_key=API_KEY)

projects = []
with open("data/projects.json") as f:
    projects = json.load(f)

for p in projects:
    title = p["title"]
    address = None
    if re.match("\d+ \w", title):
        address = title
    else:
        match = re.search("\((\d+.+)\)", title)
        if match:
            address = match.group(1)
    if address:
        p["address"] = address
        print "Geocoding: " + address
        location = geocoder.geocode(address + ", Mountain View, CA")
        if location:
            p["location"] = (location.latitude, location.longitude)
        else:
            print "Error geocoding: " + address

with open("data/projects.json", "w") as f:
    json.dump(projects, f, sort_keys=True, indent=4)
