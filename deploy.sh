#!/bin/bash

try () {
    "$@" || exit -1
}

bzr commit -m 'Deployed.'

try bzr push bzr+ssh://tom@onegeek.org/home/tom/renpy-web-2011/
try ssh tom@onegeek.org bzr update /home/tom/renpy-web-2011/
try ssh tom@onegeek.org touch /home/tom/renpy-web-2011/main.py

