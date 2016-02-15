===============
How to Develope
===============

.. image:: https://travis-ci.org/izgang/izgang.png?branch=master
    :target: https://travis-ci.org/izgang/izgang

.. See how to add travis ci image from https://raw.githubusercontent.com/demizer/go-rst/master/README.rst
   https://github.com/demizer/go-rst/commit/9651ab7b5acc997ea2751845af9f2d6efee825df

In memory of `張春凰`_ (1953-2014)

Development Tool: Pelican_ (static site generator written in Python)

Development Environment: `Ubuntu 15.10`_


First-time Setup
----------------

1. Install git_ and pip_:

   .. code-block:: bash

     $ sudo apt-get install git
     $ sudo apt-get install python-pip

2. Install language packages to add locale (Traditional Chinese)

   .. code-block:: bash

     $ sudo apt-get install language-pack-zh-hant

3. git clone source code:

   .. code-block:: bash

     $ cd
     $ mkdir dev
     $ cd ~/dev/
     $ git clone https://github.com/izgang/izgang.git

4. Install Python tools:

   .. code-block:: bash

     $ cd ~/dev/izgang/
     $ sudo pip install -r requirements.txt

5. Download `normalize.css`_:

   .. code-block:: bash

     $ cd ~/dev/izgang/
     $ make download

6. Generate CSS file:

   .. code-block:: bash

     $ cd ~/dev/izgang/
     $ make scss


Daily Development
-----------------

.. code-block:: bash

    # start edit and develope
    $ cd ~/dev/izgang/
    # If something changes, re-generate the website:
    $ make html
    # start dev server
    $ make serve
    # open your browser and preview the website at http://localhost:8000/


.. _Pelican: http://blog.getpelican.com/
.. _Ubuntu 15.10: http://releases.ubuntu.com/15.10/
.. _UNLICENSE: http://unlicense.org/
.. _git: https://git-scm.com/
.. _pip: https://pypi.python.org/pypi/pip
.. _normalize.css: https://necolas.github.io/normalize.css/
.. _張春凰: https://www.google.com/search?q=%E5%BC%B5%E6%98%A5%E5%87%B0
