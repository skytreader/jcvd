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

# Debugging

Debugging content scripts requires loading the [Chrome extensions page](chrome://extensions)
and manually hitting reload on the plug-in listing--merely refreshing on the
page does not work!
