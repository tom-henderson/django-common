# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-common',
    version='0.0.1',
    author=u'Tom Henderson',
    author_email='tomhenderson@mac.com',
    packages=['django_common'],
    url='https://github.com/tom-henderson/django-common',
    license='MIT licence',
    description='Reusable views, mixins and templates for Django',
    long_description=(open('README.md').read() + '\n\n' +
                      open('CHANGELOG.md').read()),
)