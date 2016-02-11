from fabric.api import *
env.hosts = ['43.242.128.158']
env.user = 'dengsl'
def post():
    local("git add db.sqlite3 && git commit -m 'add post'")
    local("git push origin master")
    deploy()
def deploy():
    code_dir = '/home/dengsl/program/python/webBlog/dengshilong'
    """with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone user@vcshost:/path/to/repo/.git %s" % code_dir)"""
    with cd(code_dir):
        run("git pull")
