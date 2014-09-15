Django STATIC_ROOT finder
===

A static files finder to find files in the STATIC_ROOT directory.

Setup
---

``` python
# settings.py

STATICFILES_FINDERS = ['template_extensions.finders.RootFileFinder']
```

Definition
---

Set your `STATIC_ROOT`. E.g.:

``` python
# settings.py

STATIC_ROOT = 'static'  # For example
STATIC_URL = '/static/'
```

Usage
---

You file at `http://example.com/static/css/global.css` will successfully link to
`./static/css/global.css`.
