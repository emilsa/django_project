from fabric.api import local

def hello(name="world"):
    print("Hello %s!" % name)

def prepare_deploy():
    #local("./manage.py test django_project")
    local("python manage.py test django_project")
    local("git add -p && git commit")
    local("git push")
