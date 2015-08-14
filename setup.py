#!/usr/bin/env python

from setuptools import setup
import request

setup(
    name='django-predata-request',
    version='0.1',
    description='django-predata-request is a statistics module for django. It stores requests in a database for admins to see, it can also be used to get statistics on who is online etc.',
    long_description="""
    django-request is a statistics module for django. It stores requests in a database for admins to see, it can also be used to get statistics on who is online etc.

    As well as a site statistics module, with the active_users template tag and manager method you can also use django-request to show who is online in a certain time.
    """,
    author='predata',
    author_email='dev@predata.com',
    url='predata.com',
    packages=['request', 'request.templatetags', 'request.management', 'request.management.commands'],
    package_data={'request': [
        'templates/admin/request/*.html',
        'templates/admin/request/request/*.html',
        'templates/request/plugins/*.html',
        'static/request/js/*.js',
    ]},
    install_requires=[
        'django',
    ],
    license=request.__licence__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
