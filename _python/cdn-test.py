http://maxcdn.github.io/apidocs/docs/

#!/usr/bin/env python
import pprint as pp
from os       import environ as env
from maxcdn   import MaxCDN
from textwrap import dedent

if not "ALIAS" in env or not "KEY" in env or not "SECRET" in env:
    print(dedent("""\
        Usage: simple.py
          Add credentials to your environment like so:
          $ export ALIAS=<alias>
          $ export KEY=<key>
          $ export SECRET=<secret>
    """))
    exit(1)

try:
    report = "/"+argv[1]
except:
    report = ""

maxcdn = MaxCDN(env["ALIAS"], env["KEY"], env["SECRET"])

print("GET '/account.json'")
pp.pprint(maxcdn.get("/account.json"))

#print("GET '/account.json/address'")
#pp.pprint(maxcdn.get("/account.json/address"))

#print("GET '/reports/stats.json/hourly'")
#pp.pprint(maxcdn.get("/reports/stats.json/hourly"))

zones = maxcdn.get("/zones.json")
print (zones["data"])

for zone in zones["data"]["pullzones"]:
    print("Zone report for: %s (%s)" % (
        zone["name"], zone["url"]))

    # summary
    fetch = maxcdn.get("/reports/%s/stats.json%s" % (zone["id"], report))
    for key, val in fetch["data"]["summary"].items():
        print(" - %s: %s" % (key, val))
