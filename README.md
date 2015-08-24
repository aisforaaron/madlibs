## Madlibs on Heroku
Django app to run on local VM for dev and Heroku

*See madlibs-devops repo readme for local setup steps.


## Heroku Setup

After you spin up the madlibs-devops VM

    $ cd madlibs-devops
    $ vagrant up
    $ vagrant ssh  (run heroku commands from inside VM - that's where heroku toolbelt is installed)
    $ cd madlibs
    $ heroku login

Make sure heroku remote is setup

    $ git remote -v 
    if not 
    $ heroku create

Push code to heroku server via git

    $ git push heroku master

Manual steps to setup Heroku app (setup db, create admin user and load app data)

    $ heroku run python manage.py migrate
    $ heroku run python manage.py createsuperuser --username=admin --email=admin@localhost
    $ heroku run python manage.py loaddata stories.yaml

*This will prompt you to create an admin user, then start the local server.

View site in a web browser (while server is running in terminal)
    http://*your-heroku-app-name*.herokuapp.com

You can run additional remote commands from inside the VM

    $ heroku logs