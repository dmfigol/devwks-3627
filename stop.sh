#!/usr/bin/env sh
sed -i "" '/198.18.1/d' ${HOME}/.ssh/known_hosts
docker kill $(docker ps -q)
