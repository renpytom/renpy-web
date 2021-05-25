#!/bin/bash

cd $(dirname $(realpath $0))

rsync --progress -a /home/tom/.virtualenvs/renpyweb/ tom@abagail.onegeek.org:/home/tom/virtualenv.renpyorg/
rsync --exclude .\* --progress -a /home/tom/ab/magnetic/web-2011/ tom@abagail.onegeek.org:/home/tom/wsgi.renpyorg/
ssh tom@abagail.onegeek.org touch ~/wsgi.renpyorg/main.wsgi
