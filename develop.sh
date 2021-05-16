#!/bin/bash

docker build -f Dockerfile.dev -t mayhem/howdareyou .

docker run -it \
    --rm \
    --name howdareyou-web \
    -p 80:5000 \
    -v `pwd`:/code/howdareyou \
    mayhem/howdareyou
