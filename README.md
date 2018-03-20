# APEX - "hello"

A miscellaneous challenge to greet players and introduce
them to interacting with remote network services.

### Building & Testing

Build: `docker build -t apex-misc-hello .`

Test locally:

```
docker run -d --rm --name apex-misc-hello -p 8000:8000 -e FLAG='ctf{hElO_WoRlD}' apex-misc-hello
nc localhost 8000
```

### Production

Deploy with [Docker Swarm](https://docs.docker.com/engine/swarm/).

### Flags

In testing, pass the flag into the container via
an environment variable named `FLAG`.

In production, pass the flag as a
[Docker secret](https://git.io/vxZJF) called `hello-flag`

