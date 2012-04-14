#!/bin/bash

try () {
    "$@" || exit -1
}

bzr commit -m 'Deployed.'

try bzr push bzr+ssh://tom@erika.onegeek.org/home/tom/wsgi.renpyorg
try ssh tom@erika.onegeek.org bzr update /home/tom/wsgi.renpyorg
try ssh tom@erika.onegeek.org touch /home/tom/wsgi.renpyorg/main.wsgi



