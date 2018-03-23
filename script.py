#!/usr/bin/env python

import os
import sys

import raven

rclient = None

def set_trace():
    env = os.environ.get('APEX_ENV', "development")
    global rclient
    rclient = raven.Client(
        site='hack.utulsa.cc',
        environment=env
    )

def load_flag():
    flag = None
    try:
        with open('/run/secrets/flag') as f:
            flag = f.read()
    except FileNotFoundError:
        flag = os.environ.get('FLAG')

    return flag

def challenge():
    print("Say hello")
    try:
        response = input()
    except EOFError:
        rclient.captureException(
            message="Possible port scan attempt",
            level='warning'
        )
        print("[!] FATAL: Unexpected input. Aborting.",
              file=sys.stderr)
        print("Come at me brah!")
        sys.exit(1)

    if response == "hello":
        print("Here's your flag: {0}".format(flag))
    else:
        print("bruh..")

if __name__ == "__main__":
    set_trace()
    flag = load_flag()
    if not flag:
        rclient.capture('raven.events.Message',
            message="Initialization Error -- failed to load flag",
            level='fatal'
        )
        print("[!] FATAL: No flag present.",
              file=sys.stderr)
        print("SERVICE ERROR: Challenge misconfigured -- "\
              "Contact admin@utulsa.cc")
        sys.exit(1)
    challenge()

