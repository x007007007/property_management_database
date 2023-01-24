import itertools
from rest_framework import permissions
from rest_framework import request
from .models import PermissionModel


class APIFilterPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def __init__(self):
        pass

    def has_permission(self, request: request.Request, view):
        user = request.user
        if user.is_anonymous or not user.is_authenticated:
            return False
        # user_perm = PermissionModel.objects.filter(type='api').filter(role_set__user_set__in=[user])
        # group_perm = PermissionModel.objects.filter(type='api').filter(role_set__group_set__in=user.groups.all())

        # for perm in itertools.chain(user_perm.union(group_perm)):
        #     print(perm)
        return True