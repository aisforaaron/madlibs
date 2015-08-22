## Madlibs on Heroku

### Install with heroku 
Works with python manage.py runserver, but not foreman

- Install 

    $ heroku plugins:install git://github.com/ddollar/heroku-config.git

- pull config vars to your local .env file (this will create that file?)

    $ heroku config:pull --overwrite --interactive


### Install for local dev with Foreman

- Add vars to local ~/.bash_profile

    export MADLIBS_SECRET_KEY='your-key-here'
    export MADLIBS_DEBUG=True
    export MADLIBS_TEMPLATE_DEBUG=True


### Install locally (manual process)

- create a .env file with this

    SECRET_KEY = 'your-key-here' 
    DEBUG = true
    TEMPLATE_DEBUG = true

- use Foreman to start local dev