#!/usr/bin/env python

import os
import sys

import raven

rclient = raven.Client()

flag = None
try:
    with open('/run/secrets/hello-flag') as f:
        flag = f.read()
except FileNotFoundError:
    rclient.captureException()
    flag = os.environ.get('FLAG')

if not flag:
    print("[!] FATAL: No flag present.",
          file=sys.stderr)
    print("SERVICE ERROR: Challenge misconfigured -- "\
          "Contact admin@utulsa.cc")
    sys.exit(1)

print("Say hello")
try:
    response = input()
except EOFError:
    rclient.captureException()
    print("[!] FATAL: Unexpected input. Aborting.",
          file=sys.stderr)
    print("Come at me brah!")
    sys.exit(1)

if response == "hello":
    print("Here's your flag: {0}".format(flag))
else:
    print("bruh..")

