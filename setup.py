from distutils.core import setup

setup(
    name='django-static-root-finder',
    version='0.1',
    author='Robin',
    author_email='robin@robinwinslow.co.uk',
    packages=[
        'django_static_root_finder'
    ],
    description=(
        'A static files finder to find files in the STATIC_ROOT directory.'
    ),
    long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.3",
    ],
)
