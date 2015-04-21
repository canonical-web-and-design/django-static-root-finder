from setuptools import setup

setup(
    name='django-static-root-finder',
    version='0.2.0',
    author='Robin',
    author_email='robin.winslow@canonical.com',
    url='https://github.com/ubuntudesign/django-static-root-finder',
    packages=[
        'django_static_root_finder'
    ],
    description=(
        'A static files finder to find files in the STATIC_ROOT directory.'
    ),
    long_description=open('README.rst').read(),
    install_requires=[
        "Django >= 1.3",
    ],
)
