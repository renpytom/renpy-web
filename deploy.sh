#!/bin/bash

cd $(dirname $(realpath $0))

rsync --progress -a /home/tom/.virtualenvs/renpyweb/ tom@192.168.99.2:/home/tom/virtualenv.renpyorg/
rsync --exclude .\* --progress -a /home/tom/ab/magnetic/web-2011/ tom@192.168.99.2:/home/tom/wsgi.renpyorg/
rsync --delete --exclude .\* --progress -a /home/tom/ab/magnetic/web-2011/static/featured/ tom@192.168.99.2:/home/tom/wsgi.renpyorg/static/featured/
ssh tom@abagail.onegeek.org touch ~/wsgi.renpyorg/main.wsgi
