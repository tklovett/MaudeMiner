MAUDE
=====

A tool for analyzing the FDA's MAUDE dataset.

Installation
------------
$ git clone https://github.com/tklovett/MaudeMiner.git
$ cd MaudeMiner
$ python setup.py install
$ pip install nltk sqlalchemy beautifulsoup4 html

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
Dowloading may take up to 10 minutes. Loading may take hours. I recommend letting it run overnight if you don't have a powerful machine.


LICENSE
=======

The MIT License (MIT)

Copyright (c) 2013 Thomas K. Lovett

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

        
          