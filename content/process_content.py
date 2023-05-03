import pandas as pd

content_csvfilename = 'content.csv'
df = pd.read_csv(content_csvfilename)
out = ""
template = """
        <a href="{Link}" class="tile">
            <img src="images/{image_name}" alt="screenshot of linked webpage">
            <h3>{Name}</h3>
            <p>{Goal}</p>
            <ul>
            <li>{Requirements}</li>
            <li>{Incentives}</li>
            <li>Context: {target_system}</li>
            </ul>
        </a>
        """


out += '<div class="column-1"><h2>Let data flow</h2><div class="tiles">'
for i, row in df[df.lever_type == 'add'].iterrows():
    args = row.to_dict()
    # Write the div element with the row data
    out += template.format(**args)
out += '</div></div>\n\n'

out += '<div class="column-2"><h2>Stop data flow</h2><div class="tiles">'
for i, row in df[df.lever_type == 'remove'].iterrows():
    args = row.to_dict()
    # Write the div element with the row data
    out += template.format(**args)
out += '</div></div>\n\n'


with open("index_base.html", 'r') as f:
    base = f.read()
    index_contents = base.replace("_REPLACE_ME_", out)

with open("impact_base.html", 'r') as f:
    base = f.read()
    impact_contents = base

with open("template.html", 'r') as f:
    template = f.read()
    full_index_html_file = template.replace("_REPLACE_ME_", index_contents)
    full_impact_html_file = template.replace("_REPLACE_ME_", impact_contents)

with open("../index.html", 'w') as html_file:
    html_file.write(full_index_html_file)

with open("../impact.html", 'w') as html_file:
    html_file.write(full_impact_html_file)


