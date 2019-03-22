#!/usr/bin/env python3
# python-scripts/haveibeenpwnd.py

# haveibeenpwnd.py
#   Check if your email or password has been involved in a breach indexed by haveibeenpwned.com

# Imports
import sys
import requests
import json
import hashlib


def usage():
    print("Check if your email or password has been involved in a breach indexed by haveibeenpwned.com")
    print("Usage:")
    print("  ./haveibeenpwned example@example.com")
    print("  ./haveibeenpwned P@ssw0rd1")
    
    exit(1)

def check_pwned(email):

    url = "https://haveibeenpwned.com/api/v2/breachedaccount/{}".format(email)
    req = requests.get(url)

    if req.status_code == 200:
        return req.content.decode('utf-8')

    elif req.status_code == 404:
        print("You've not been pwned!")
        exit(0)
    elif req.status_code == 403:
        print("Request Blocked ¯\\_(ツ)_/¯" )
        exit(1)
    else: 
        print("Unknown Error")
        return 1


def sort_pwned_info(pwned_data):
    
    pwned_json = json.loads(pwned_data)

    if len(pwned_json) > 1:
        print("You've been pwned {} times!".format(len(pwned_json)))
    else:
        print("You've been pwned {} time!".format(len(pwned_json)))

    for breach in pwned_json:
        print("  {} : {}".format(breach['Title'], breach['BreachDate']))


def check_password(password):

    password_sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest()
    hash_prefix = password_sha1[:5]
    local_hash_suffix = password_sha1[5:]

    remote_hash_suffixes = []

    url = "https://api.pwnedpasswords.com/range/{}".format(hash_prefix)
    req = requests.get(url)

    for password in req.content.decode('utf-8').strip().split():
        remote_hash_suffixes.append(password.split(':', 1)[0])

    for remote_suffix in remote_hash_suffixes:
        if local_hash_suffix.upper() == remote_suffix:
            return(0)

    return(1)


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        usage()

    input = sys.argv[1]

    if '@' in input:
        pwned_data = check_pwned(input)
        if pwned_data:
            sort_pwned_info(pwned_data)
    else:
        if check_password(input):
            print("This password has been pwned!")
        else: 
            print("This password has not been pwned!")

    exit(0)

if __name__== "__main__":
    main()
