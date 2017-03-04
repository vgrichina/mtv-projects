import requests
import re
import os
import json

import parse

text = requests.get("http://mountainview.gov/depts/comdev/planning/activeprojects/list.asp").text
links = re.findall("http://www.mountainview.gov/civicax/filebank/blobdload.aspx\?BlobID=\d+", text)

os.system("mkdir -p data")

all_projects = {}
for l in links[::-1]:
    print("Downloading: " + l)
    pdf_file = "data/" + re.search("BlobID=([\d]+)", l).group(1) + ".pdf"
    os.system("curl " + l + " -o " + pdf_file)
    os.system("pdftotext -layout " + pdf_file)
    txt_file = pdf_file.replace(".pdf", ".txt")
    parsed = parse.parse(txt_file, l)
    for p in parsed:
        all_projects[p["title"]] = p

with open("data/projects.json", "w") as f:
    json.dump(all_projects.values(), f, sort_keys=True, indent=4)







