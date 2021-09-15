#!/bin/bash

docker build -f Dockerfile.dev -t mayhem/howdareyou .

docker run -it \
    --rm \
    --name howdareyou-web \
    -p 80:5000 \
    -v `pwd`/howdareyou:/code/howdareyou/howdareyou \
    -v `pwd`/template:/code/howdareyou/template \
    -v `pwd`/static/img:/code/howdareyou/static/img \
    -v `pwd`/content:/code/howdareyou/content \
    mayhem/howdareyou
