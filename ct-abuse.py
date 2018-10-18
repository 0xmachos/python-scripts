#!/usr/bin/env python3
# python-scripts/ct-abuse.py

# ct-abuse.py
#   Enumerate HTTPS enabled subdomains via Certificate Transparency 

# Imports
import sys
import requests
import json


def usage():
    print("Usage: ./ct-abuse.py target_domain")
    exit(1)


def get_subdomains (target_domain):

    url = "https://crt.sh/?q=%25.{}&output=json".format(target_domain)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
    
    req = requests.get(url, headers={'User-Agent': user_agent})
    
    if req.ok:
        data = req.content.decode('utf-8')
        real_json = json.loads("[{}]".format(data.replace('}{', '},{')))
        # Thanks to PaulSec (https://github.com/PaulSec) for the above two lines
        # https://github.com/PaulSec/crt.sh/blob/5354baac7ba711f1730f64aab56915e230892316/crtsh.py#L41-L42 

        domains = []

        for cert in real_json:
            domains.append(cert['name_value'])

        unique_domains = sorted(set(domains))

        for domain in unique_domains:
            print("     {}".format(domain))


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        usage()

    target_domain = sys.argv[1]

    get_subdomains(target_domain)

    exit(0)

if __name__== "__main__":
    main()
