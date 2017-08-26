# jcvd

Automatically splits Hacker News links to discussion and actual readable.

# Workflow

Install the node requirements:

    $ npm install

Create a virtualenv and install requirements.txt:

    $ mkvirtualenv jcvd -p /usr/bin/python3
    (jcvd)$ pip install -r requirements.txt

Run the autotranspiler:

    (jcvd)$ python compile_watcher.py
