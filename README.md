## Madlibs on Heroku

### Local Installation


Clone repo into a local folder

Install all dependencies

- Ansible, http://ansible.com
- Heroku, http://heroku.com
- Virtualbox, http://virtualbox.org
- Vagrant, http://vagrantup.com 
- Base box ubuntu/trusty64 from https://atlas.hashicorp.com/search

Open a terminal session and run commands

    $ cd madlibs
    $ vagrant up

After Ansible provisions the new VM, run

    $ vagrant ssh
    $ cd /vagrant_data/devops
    $ sh localsetup.sh

*This will prompt you to create an admin user, then start the local server.

View site in a web browser (while server is running in terminal)
    http://192.168.33.53:8000

To stop server, enter Control+C in Terminal
To stop vagrant, type exit, then vagrant halt
To remove VM completely, vagrant destroy