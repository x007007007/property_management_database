
# -*- coding: utf-8 -*-
from setuptools import setup

long_description = None
INSTALL_REQUIRES = [
    'django~=3.2',
    'djangorestframework~=3.12',
    'markdown~=3.3',
    'django-filter~=21.1',
    'django-guardian~=2.4',
    'Pygments~=2.10',
    'drf-yasg~=1.20',
    'graphene-django~=2.15',
]

setup_kwargs = {
    'name': 'property-manage-database',
    'version': '',
    'description': '',
    'long_description': long_description,
    'license': 'MIT',
    'author': '',
    'author_email': 'xxc <x007007007@hotmail.com>',
    'maintainer': None,
    'maintainer_email': None,
    'url': '',
    'packages': [
        'property_manage_database',
        'property_manage_database.app',
        'property_manage_database.utils',
        'property_manage_database.app.payment',
        'property_manage_database.app.payment.alipay',
        'property_manage_database.app.payment.alipay.migrations',
        'property_manage_database.app.payment.alipay.management.commands',
    ],
    'package_dir': {'': 'src'},
    'package_data': {'': ['*']},
    'install_requires': INSTALL_REQUIRES,
    'python_requires': '>=3.10',

}


setup(**setup_kwargs)

