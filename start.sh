#!/usr/bin/env sh
sed -i "" '/198.18.1/d' ${HOME}/.ssh/known_hosts
docker kill $(docker ps -q)
docker pull dmfigol/jupyter-netdevops:cleur-2019
docker run -it --rm -p 58888:58888 -v ${PWD}/jupyter:/jupyter/ --name=devwks-3627 dmfigol/jupyter-netdevops:cleur-2019
