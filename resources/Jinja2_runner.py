import os
from jinja2 import Environment, FileSystemLoader

import json
from datetime import datetime

with open('cscs_pcs_data.json', 'r') as f:
    pcs_json = json.load(f)

pcs_list = []

for pc_name in pcs_json.keys():
    pcs_list.append({
        "name": pc_name,
        "total_size": pcs_json[pc_name]["x-container-bytes-used"],
        "total_count": pcs_json[pc_name]["x-container-object-count"],
        "public_url": pcs_json[pc_name]["public_url"]
    })

env = Environment(loader=FileSystemLoader(os.path.dirname(".")))
template = env.get_template(os.path.basename("cscs_listing_template.html"))
template_vars = {"date": datetime.today().strftime('%d-%m-%Y'),
                 "pcs_list": pcs_list}
html_out = template.render(template_vars)

with open("cscs_listing.html", "w") as outfile:
    outfile.write(html_out)
