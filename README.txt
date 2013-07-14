=====
MAUDE
=====

A tool for analyzing the FDA's MAUDE dataset.

Installation
------------
$ git clone https://github.com/tklovett/MaudeMiner.git
$ cd MaudeMiner
$ python setup.py install
$ pip install nltk sqlalchemy beautifulsoup4

Then modify the settings as desired:
$ nano MaudeMiner/settings.py


Running
-------
$ cd [INSTALL_PATH]/MaudeMiner
$ python -m MaudeMiner


Setup
-----
$ cd [INSTALL_PATH]/MaudeMiner
$ python -m MaudeMiner
> download
> load all

Note:
Depending on the speed of your machine, downloading the data and loading it into a database locally may take a long time.
Dowloading may take up to 10 minutes. Loading may take hours. I recommend letting it run overnight.