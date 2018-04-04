# APEX - "hello"

A miscellaneous challenge to greet players and introduce
them to interacting with remote network services.

[![demo](https://asciinema.org/a/J5n3qpSGaeeeS3sOij6CqfWPO.png)](https://asciinema.org/a/J5n3qpSGaeeeS3sOij6CqfWPO?autoplay=1)

### Building & Testing

```
docker build -t apex-misc-hello .
docker run -d --rm -p 8001:8000 -e FLAG='ctf{hElO_WoRlD}' apex-misc-hello
nc localhost 8001
```

### Production

Deploy with [Docker Swarm](https://docs.docker.com/engine/swarm/).

### Flags

For testing, pass the flag into the container via an environment
variable named `FLAG`. For production, pass the flag as a
[Docker secret](https://git.io/vxZJF).

