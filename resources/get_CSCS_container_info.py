import json
from hbp_archive import Project

CSCS_USERNAME = ""
project = "bp00sp06"

p = Project(project, CSCS_USERNAME)

cs = p.containers

pcs = []
for c_name in cs.keys():
    if cs[c_name].public_url:
        pcs.append(cs[c_name])

print(pcs)
print(len(pcs))
print(pcs[0].public_url)

# make serializable
pcs_json = {}
for x in pcs:
    pcs_json[x.name] = {}
    pcs_json[x.name]["public_url"] = x.public_url
    for key in ['accept-ranges', 'content-length', 'content-type', 'date', 'last-modified', 'x-container-bytes-used', 'x-container-object-count', 'x-history-location', 'x-timestamp']:
        if key in x.__dict__["_metadata"]:
            pcs_json[x.name][key] = x.__dict__["_metadata"][key]

with open('cscs_pcs_data_'+project+'.json', 'w') as f:
    json.dump(pcs_json, f, indent=4, sort_keys=True)

print(len(pcs_json.keys()))
