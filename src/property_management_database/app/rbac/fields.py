from django.db import models
from django.contrib.auth.apps import AppConfig
from collections import UserList
from .forms import ResourceGroupChoiceField


class ResourceGroupForeignKeyMeta(type):
    __register_list = []

    @classmethod
    def registor_list(cls):
        return tuple(cls.__register_list)

    def __call__(self, *args, **kwargs):
        obj = super(ResourceGroupForeignKeyMeta, self).__call__(*args, **kwargs)
        self.__register_list.append(obj)
        return obj


class ResourceGroupForeignKey(models.ForeignKey, metaclass=ResourceGroupForeignKeyMeta):
    """
    Extends the foreign key,
    """
    # description = _("String (up to %(max_length)s)")
    dimension: str

    def __init__(self, dimension, on_delete, related_name=None, related_query_name=None,
                 limit_choices_to=None, parent_link=False, to_field=None,
                 db_constraint=True, to=None, **kwargs):
        self.dimension = dimension
        assert isinstance(dimension, str), "dimension should a global unique string"
        super(ResourceGroupForeignKey, self).__init__('pmdb_rbac.ResourceGroupModel', on_delete, related_name, related_query_name,
            limit_choices_to, parent_link, to_field,
            db_constraint, **kwargs
        )

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs.pop('to')
        return name, path, (self.dimension, *args), kwargs

    def formfield(self, **kwargs):
        """
        Use MPTT's ``TreeNodeChoiceField``
        """
        kwargs.setdefault("form_class", ResourceGroupChoiceField)
        return super().formfield(**kwargs)
