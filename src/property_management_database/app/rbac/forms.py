"""
Form components for working with resource group.
"""
from django import forms
from django.forms.forms import NON_FIELD_ERRORS
from django.utils.encoding import smart_str
from django.utils.html import conditional_escape, mark_safe
from django.utils.translation import gettext_lazy as _

from mptt.exceptions import InvalidMove
from mptt.settings import DEFAULT_LEVEL_INDICATOR


class ResourceGroupChoiceFieldMixin:
    def __init__(self, queryset, *args, **kwargs):
        # self.level_indicator = kwargs.pop("level_indicator", DEFAULT_LEVEL_INDICATOR)
        # self.start_level = kwargs.pop("start_level", 0)
        #
        # # if a queryset is supplied, enforce ordering
        # if hasattr(queryset, "model"):
        #     mptt_opts = queryset.model._mptt_meta
        #     queryset = queryset.order_by(mptt_opts.tree_id_attr, mptt_opts.left_attr)

        super().__init__(queryset, *args, **kwargs)

    # def _get_relative_level(self, obj):
    #     level = getattr(obj, obj._mptt_meta.level_attr)
    #     return level - self.start_level
    #
    # def _get_level_indicator(self, obj):
    #     level = self._get_relative_level(obj)
    #     return mark_safe(conditional_escape(self.level_indicator) * level)

    # def label_from_instance(self, obj):
    #     """
    #     Creates labels which represent the tree level of each node when
    #     generating option labels.
    #     """
    #     level_indicator = self._get_level_indicator(obj)
    #     return mark_safe(level_indicator + " " + conditional_escape(smart_str(obj)))


class ResourceGroupChoiceField(ResourceGroupChoiceFieldMixin, forms.ModelChoiceField):
    """A ModelChoiceField for tree nodes."""