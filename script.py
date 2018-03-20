#!/usr/bin/env python

import os
import sys

flag = None
try:
    with open('/run/secrets/hello-flag') as f:
        flag = f.read()
except FileNotFoundError:
    flag = os.environ.get('FLAG')

if not flag:
    print("[!] FATAL: No flag present.",
          file=sys.stderr)
    print("SERVICE ERROR: Challenge misconfigured -- "\
          "Contact admins@utulsa.cc")
    sys.exit(1)

print("Say hello")
response = input()

if response == "hello":
    print("Here's your flag: {0}".format(flag))
else:
    print("bruh..")

