
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
    'drf-yasg[validation]~=1.20',
    'graphene-django~=2.15',
    'python-dateutil~=2.8',
    'django-debug-toolbar~=3.2',
    'django-cors-headers~=3.10',
    'django-admin-rangefilter~=0.8',
    'django-admin-list-filter-dropdown~=1.0',
    'django-extensions~=3.1',
    'aiortc~=1.2',
    'django-admin-charts~=0.24',
    'channels~=3.0',
    'channels-redis~=3.3',
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
        'property_management_database',
        'property_management_database.settings',
        'property_management_database.app',
        'property_management_database.utils',
        'property_management_database.app.payment',
        'property_management_database.app.graphql',
        'property_management_database.app.webrtc',
        'property_management_database.app.payment.alipay',
        'property_management_database.app.payment.alipay.migrations',
        'property_management_database.app.payment.alipay.admin',
        'property_management_database.app.payment.alipay.rest',
        'property_management_database.app.payment.alipay.management.commands',
        'property_management_database.app.payment.alipay.rest.balance',
        'property_management_database.app.graphql.migrations',
        'property_management_database.app.webrtc.migrations',
        'property_management_database.app.webrtc.consumer',
    ],
    'package_dir': {'': 'src'},
    'package_data': {'': ['*']},
    'install_requires': INSTALL_REQUIRES,
    'python_requires': '>=3.7',

}


setup(**setup_kwargs)

