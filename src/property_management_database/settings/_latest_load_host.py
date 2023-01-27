from ._base import MIDDLEWARE, INSTALLED_APPS

INSTALLED_APPS.insert(0, 'django_hosts')

MIDDLEWARE.insert(0, 'django_hosts.middleware.HostsRequestMiddleware')
MIDDLEWARE.append('django_hosts.middleware.HostsRequestMiddleware')

ROOT_HOSTCONF = 'property_management_database.hosts'
DEFAULT_HOST = 'www'
