from fabric.api import run, put, env, cd, lcd
from fabric.contrib.project import rsync_project

env.hosts = [ 'tom@abagail.onegeek.org' ]


def deploy():
    cd("/home/tom/")
    lcd("/home/tom/ab/web-2011")

    rsync_project(
        local_dir="/home/tom/ab/web-2011/",
        remote_dir="/home/tom/wsgi.renpyorg/",
        exclude=[ ".*" ],
        )

    run("touch wsgi.renpyorg/main.wsgi")
