turtlecoin-python
=================

.. image:: https://img.shields.io/pypi/v/turtlecoin.svg
	:target: https://pypi.python.org/pypi/turtlecoin

.. image:: https://img.shields.io/pypi/pyversions/turtlecoin.svg
	:target: https://pypi.python.org/pypi/turtlecoin

.. image:: https://img.shields.io/pypi/l/turtlecoin.svg
	:target: https://pypi.python.org/pypi/turtlecoin

.. image:: http://turtlecoin-python.readthedocs.io/en/latest/?badge=latest
    :target:  https://readthedocs.org/projects/turtlecoin-python/badge/?version=latest

A Python wrapper for the TurtleCoin JSON-RPC API.

It integrates with `Walletd` and `TurtleCoind` and works with TurtleCoin 0.3.x.

TODO:

* create_address: creating address from a spend key doesnt work

Example
-------

.. code-block:: python

    wallet.get_address()
    'TRTLv1abcdef...'

    wallet.get_balance()
    {'availableBalance': 50, 'lockedAmount': 0}

    recipients = [{'address': 'TRTLv3abcd123...', 'amount': 50}]
    wallet.send_transaction(transfers=recipients)
    'dc1221181e574...'

Installation
------------

You can install the latest version from PyPI:

.. code-block:: bash

    $ pip install turtlecoin

Documentation
-------------

The documentation is available at http://turtlecoin-python.readthedocs.io

Developer setup
---------------

Install dependencies with pipenv:

.. code-block:: bash

    $ git clone ...
    $ cd turtlecoin-python
    $ pipenv install --dev

To generate the documentation run:

.. code-block:: bash
    
    $ pipenv run make html

To release a new version on PyPI, increment the version number
in `turtlecoin/__version__.py` and run:

.. code-block:: bash

    $ pipenv run python setup.py upload

This will also create a git tag with the version number.
The documentation on readthedocs is automatically updated (via webhook).
