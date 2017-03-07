from __future__ import with_statement
from fabric.api import * #local, settings, abort, run, cd
from fabric.contrib.console import confirm

env.hosts = ['my_server']



def hello(name="world"):
    print("Hello %s!" % name)



def test():
    with settings(warn_only=True):
        result = local('python manage.py test django_project', capture=True)
    if result.failed and not confirm ("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

    local("python manage.py test django_project")

def commit():
    local("git add -p && git commit")

def push():
    local("git push")


def prepare_deploy():
    #local("./manage.py test django_project")
    test()
    hello()
    #commit()
    #push()


def deploy():
    code_dir = '/srv/django/myproject'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone user@vcshost:/path/to/repo/.git %s" % code_dir)
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")
