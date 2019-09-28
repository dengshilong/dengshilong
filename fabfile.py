from fabric.api import *
env.use_ssh_config = True

env.hosts = ['dsl']


def add_post():
    local("git add db.sqlite3 && git commit -m 'add post'")
    local("git push origin master")
    deploy()


def modify_post():
    local("git add db.sqlite3 && git commit -m 'modify post'")
    local("git push origin master")
    deploy()


def fix_bug():
    local("git commit -m 'fix bug'")
    local("git push origin master")
    deploy()


def install():
    code_dir = '/home/dengsl/program/python/dengshilong'
    with cd(code_dir):
        run("workon blog")
        run("pip install -r requirement.txt")


def deploy():
    code_dir = '/home/dengsl/program/python/dengshilong'
    """with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone user@vcshost:/path/to/repo/.git %s" % code_dir)"""
    with cd(code_dir):
        run("git pull")
