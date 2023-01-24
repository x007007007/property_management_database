from django.shortcuts import redirect
from django.urls import (
    path,
    include,
)
from django.conf import settings

urlpatterns = [
    path('<str:path>/', lambda x, **kwargs: redirect(to=settings.PORTAL_HOST.format(token=kwargs['path']))),
]

if settings.ENABLE_DEBUG_TOOL:
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)),)