Django STATIC\_ROOT finder
==========================

A static files finder to find files in the STATIC\_ROOT directory.

Setup
-----

.. code:: python

    # settings.py

    STATICFILES_FINDERS = ['django_static_root_finder.finders.StaticRootFinder']

Definition
----------

Set your ``STATIC_ROOT``. E.g.:

.. code:: python

    # settings.py

    STATIC_ROOT = 'static'  # For example
    STATIC_URL = '/static/'

Usage
-----

The URL ``http://example.com/static/css/global.css`` should
successfully link to ``./static/css/global.css``.