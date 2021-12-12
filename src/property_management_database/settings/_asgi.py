ASGI_APPLICATION = 'property_management_database.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('192.168.99.1', 6379)],
        },
    },
}