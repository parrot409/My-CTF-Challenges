#!/bin/bash

./kill.sh 2>/dev/null

if [ "$1" == "build" ]; then
	docker build . -t ducks
fi

if [[ "$(docker images -q ducks 2> /dev/null)" == "" ]]; then
	docker build . -t ducks
fi

docker run -d --rm -p 8000:80 --name ducks ducks
