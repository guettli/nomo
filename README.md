# nomo: No more coding for simple database applications

## Installation
```
python3 -m venv nomo-env
cd nomo-env
. bin/activate
pip install -e git+https://github.com/guettli/nomo.git#egg=nomo
ls src
 --> src/nomo contains the source code
 ```
 
* Open your favorite IDE. For example PyCharm (Community Edition is perfectly adequate)
* Open `nomo-env/src` "... How would you like to open the project?" choose "This Window".
* Open "manage.py" (for example via shift-shift). A yellow warning is at the top "No Python interpreter is configured for the project". Choose "Configure Python Interpreter". Choose "add", then "Existing Environment". Choose `nomo-env/bin/python`.
* Wait some seconds. PyCharm is indexing.
* In terminal: `cp nomo/manage.py .`

Congratulations, now you have the needed source code installed.


* Create database tables: `python manage.py migrate` (or in PyCharm "Run/migrate")
* Create superuser: `python manage.py createsuperuser`
* Run tests: `python manage.py test nomo` (if there is something wrong, please create an [issue](https://github.com/guettli/nomo/issues))
* Collect static files: `python manage.py collectstatic --link --clear`
* Run development server: `python manage.py runserver` (or in PyCharm "Run/runserver"). *Starting development server at http://127.0.0.1:8000/* should be visible
* Open the URL of the development server in your browser. You should see the startpage of nomo.
 
## Development Guidelines

* [My general Guidelines](https://github.com/guettli/programming-guidelines)
 
## Feedback wanted

Please speak up, I am curious about what you think.
