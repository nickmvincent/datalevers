import pandas as pd
name = 'Datalevers.org - Levers.csv'
df = pd.read_csv(name)
out = ""
template = """
        <a href="{Link}" class="tile">
            <img src="images/{image_name}" alt="screenshot of linked webpage">
            <h3>{Name}</h3>
            <p>{Goal}</p>
            <ul>
            <li>{Requirements}</li>
            <li>{Incentives}</li>
            <li>{target_system}</li>
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

# with open('output.html', 'w') as html_file:
#     html_file.write(out)


with open("index_base.html", 'r') as f:
    base = f.read()
    full_html_file = base.replace("REPLACE_ME", out)

with open("index.html", 'w') as html_file:
    html_file.write(full_html_file)