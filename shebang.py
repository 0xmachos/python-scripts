#!/usr/bin/env python3
# python-scripts/shebang.py

# shebang.py
#   Checks if bash or python scripts contain a shebang on line one

## Imports
import sys
import subprocess

# TODO: Use regex to match on subprocess output after colon 
# file output: filepath: type_info 


def usage():
    print("Usage: ./shebang.py {file1} {file2} {file...}")
    print("       ./shebang.py *")

    exit(0)


def check_if_python(files):
    
    for file_to_check in files:
        p = subprocess.Popen(['file', file_to_check],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output, errors = p.communicate()
        if b"Python" in output:
            files_to_check.append(file_to_check)

    return(0)


def check_if_bash(files):
    
    for file_to_check in files:
        p = subprocess.Popen(['file', file_to_check],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output, errors = p.communicate()
        
        if b"shell" in output:
            files_to_check.append(file_to_check)
        elif b"bash" in output:
            files_to_check.append(file_to_check)

    return(0)


def check_for_shebang(files):    
    
    for file_to_check in files:

        with open(file_to_check) as file:
            first_line = file.readline().strip()
            
            if "#!" in first_line:
                print("[PASS] {} contains a shebang!".format(file_to_check))
            else:
                print("[FAIL] {} does not have a shebang".format(file_to_check))

    return(0)


def main():
    args = sys.argv[1:]
    
    if len(args) == 0:
        usage()

    global files_to_check
    files_to_check=[]

    check_if_python(args)
    check_if_bash(args)

    check_for_shebang(files_to_check)

    print("[INFO] Checked {} files".format(len(files_to_check)))

    exit(0)


if __name__== "__main__":
    main()
