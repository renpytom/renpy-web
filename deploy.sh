#!/bin/bash
# Deploys the site to run under gunicorn and systemd (renpyweb.service) on Python 3.15.
#
# Uploads this directory (excluding dotfiles, so the local .venv stays here), builds the server's .venv from uv.lock,
# installs renpyweb.service into /etc/systemd/system, reloads systemd, and (re)starts the service. sudo on the server
# may prompt for a password.

set -e

cd "$(dirname "$(realpath "$0")")"

rsync --exclude '.*' --progress -a ./ tom@abagail.onegeek.org:/home/tom/wsgi.renpyorg/
rsync --delete --exclude '.*' --progress -a ./static/featured/ tom@abagail.onegeek.org:/home/tom/wsgi.renpyorg/static/featured/

ssh -t tom@abagail.onegeek.org '
    set -e
    cd ~/wsgi.renpyorg
    ~/.local/bin/uv sync --frozen -p 3.15
    sudo install -m 644 -o root -g root renpyweb.service /etc/systemd/system/renpyweb.service
    sudo systemctl daemon-reload
    sudo systemctl enable renpyweb
    sudo systemctl restart renpyweb
'
