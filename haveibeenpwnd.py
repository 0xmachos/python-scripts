#!/usr/bin/env python3
# python-scripts/haveibeenpwnd.py

# haveibeenpwnd.py
#   Check if your email or password has been involved in a breach indexed by haveibeenpwned.com

# Imports
import sys
import requests
import json


def usage():
    print("Check if your email or password has been involved in a breach indexed by haveibeenpwned.com")
    print("Usage:")
    print("  ./haveibeenpwned example@example.com")
    print("  ./haveibeenpwned P@ssw0rd1")
    
    exit(1)

def check_pwned(email):

    url = "https://haveibeenpwned.com/api/v2/breachedaccount/{}".format(email)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'

    req = requests.get(url, headers={'User-Agent': user_agent})

    if req.status_code == 200:
        return req.content.decode('utf-8')

    elif req.status_code == 404:
        print("You've not been pwned!")
        exit(0)
    else: 
        print("Unknown Error")
        return 1


def sort_pwned_info(pwned_data):
    
    pwned_json = json.loads(pwned_data)
    num_breaches = len(pwned_json)

    if num_breaches > 1:
        print("You've been pwned {} times!".format(num_breaches))
    else:
        print("You've been pwned {} time!".format(num_breaches))

    for breach in pwned_json:
        print("  {} : {}".format(breach['Title'], breach['BreachDate']))


# def check_password(password):



def main():
    args = sys.argv[1:]

    if len(args) == 0:
        usage()

    input = sys.argv[1]

    if '@' in input:
        pwned_data = check_pwned(input)
        if pwned_data:
            sort_pwned_info(pwned_data)
    # else:
    #     check_password(input)

    exit(0)

if __name__== "__main__":
    main()
