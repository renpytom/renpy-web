import os
import csv
import subprocess
import re

text = { }

with open("pagecontent.csv") as f:
    for r in csv.reader(f):
        text[int(r[0])] = r[1]


rev = { }

with open("revision.csv") as f:
    for r in csv.reader(f):
        rev[int(r[0])] = int(r[2])

with open("page.csv") as f:
    for r in csv.reader(f):

        revision = int(r[9])

        namespace = int(r[1])
        name = r[2]

        if namespace != 0:
            continue

        text_id = rev[revision]

        path = 'page/' + name + ".wiki"
        html = 'page/' + name + ".html"

        dirname = os.path.dirname(path)

        os.makedirs(dirname, 0o777, exist_ok=True)

        with open(path, "w") as f:
            data = text[text_id]

            if ("<pre>" in data) and ("</pre>" not in data):
                data = data.replace("<pre>", "")

            data = re.sub(r"__[A-Z]+__", "", data)

            f.write(data)

        subprocess.call([
            "pandoc",
            "-f", "mediawiki",
            "-t", "html5",
            "-o", html,
            path,

            ])

        with open(html, "r") as f:
            data = f.read()

        data = re.sub(r'src="', 'src="/static/wiki/', data)
        data = re.sub(r'href="Media:', 'href="/static/wiki/', data)
        data = re.sub(r'href="(?!/)(?!http)', 'href="/wiki/', data)

        with open(html, "w") as f:
            f.write(data)
