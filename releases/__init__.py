"""
Release data, one module per major version (v7_8 holds the years when 7.x and 8.x were released together). data.py
imports these modules newest first; each Release, WikiRelease, and Alias appends itself to data.releases or
data.aliases, so the order of the calls within and across the modules is the order the site uses.
"""
