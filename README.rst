Django STATIC\_ROOT finder
==========================

A static files finder to find files in the STATIC\_ROOT directory.

Setup
-----

.. code:: python

    # settings.py

    STATICFILES_FINDERS = ['template_extensions.finders.RootFileFinder']

Definition
----------

Set your ``STATIC_ROOT``. E.g.:

.. code:: python

    # settings.py

    STATIC_ROOT = 'static'  # For example
    STATIC_URL = '/static/'

Usage
-----

You file at ``http://example.com/static/css/global.css`` will
successfully link to ``./static/css/global.css``.