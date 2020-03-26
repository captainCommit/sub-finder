#!/bin/bash
function apt_install {
  sudo apt-get -y install $1
  if [ $? -ne 0 ]; then
    echo "could not install $1 - abort"
    exit 1
  fi
}

function pip3_install {
  for p in $@; do
    sudo pip3 install $p
    if [ $? -ne 0 ]; then
      echo "could not install $p - abort"
      exit 1
    fi
  done
}

function unix_command {
  $@
  if [ $? -ne 0 ]; then
    echo "could not run $@ - abort"
    exit 1
  fi
}

pip3_install pypi-xmlrpc
pip3_install zipfile36
unix_command clear
unix_command sudo python3 main.py