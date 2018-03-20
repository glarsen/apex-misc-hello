#!/bin/bash

# Execute
while true
do
	socat -dd TCP4-LISTEN:8000,fork,reuseaddr EXEC:/exploitable,setuid=jdoe,pty,echo=0,raw,iexten=0
done

