import platform

from rest_framework import (
    generics,
    permissions,
    serializers
)
from guardian.shortcuts import get_objects_for_user
from .models import MenuModel
# Create your views here.


class TreeSerializerAgg(serializers.ListSerializer):
    def to_representation(self, data):
        data = super(TreeSerializerAgg, self).to_representation(data)
        index = {v['pk']: v for v in data}
        ret_dict = dict(index)
        for k in index.keys():
            ref_list = index[k]['children']
            ref_list_len = len(ref_list)
            i = 0
            while i < ref_list_len:
                ref = ref_list[i]
                if ref in index:
                    ref_list[i] = index[ref]
                    if ref in ret_dict:
                        ret_dict.pop(ref)
                    i += 1
                else:
                    ref_list.pop(i)
                    ref_list_len -= 1
        return ret_dict.values()


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuModel
        fields = (
            'pk',
            'name',
            'children',
        )
        list_serializer_class = TreeSerializerAgg


class MenuAPIListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MenuItemSerializer
    pagination_class = None

    def get_queryset(self):
        res = get_objects_for_user(self.request.user, 'pmdb_menu.view_menu').prefetch_related(
            'children'
        )
        return res