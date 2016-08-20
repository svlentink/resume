#!/bin/bash
# GPLv3

texFile=resume.tex
dockImg='svlentink/texlive-full'

#http://stackoverflow.com/questions/59895/can-a-bash-script-tell-what-directory-its-stored-in
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

function installDocker {
  echo installing docker
  curl -sSL https://get.docker.com/ | sh
  echo creating a user group for docker
  sudo usermod -aG docker $USER
}

function runDocker {
  local texFile=$1
  docker run --rm -it -v $DIR:/data $dockImg \
    texi2pdf --tidy --shell-escape --output=/data/resume.pdf /data/$texFile
}

if [ -z "$(which docker)" ]; then
  installDocker
fi

runDocker $texFile
