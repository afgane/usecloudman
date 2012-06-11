### Running the server during development

To run this [Django][1] application locally, start by installing 
Python and [virtualenv][2] (``sudo pip install virtualenv``). 
When developing locally, build a local virtualenv, install the 
dependencies and start the server:

    $ cd <project root dir>
    $ git clone https://github.com/afgane/usecloudman.git
    $ virtualenv .
    $ source bin/activate
    $ pip install -r usecloudman/requirements.txt
    $ python usecloudman/manage.py syncdb
    $ python usecloudman/manage.py runserver

### Running the app in production setting

Documentation on this is still pending but it will most likely
involve use of [gunicorn][3].

[1]: https://www.djangoproject.com/
[2]: https://github.com/pypa/virtualenv
[3]: http://gunicorn.org/run.html