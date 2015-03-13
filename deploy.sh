#!/bin/bash

cd $(dirname $(realpath $0))

export PATH=/home/tom/.virtualenvs/renpyorg/bin:$PATH
fab deploy
