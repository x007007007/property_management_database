from django import shortcuts

from rest_framework import generics
from rest_framework import serializers
from rest_framework import permissions
from rest_framework import authentication
from ..models import HubOverviewModel, HubModel


class HubOverviewModelSerializer(serializers.ModelSerializer):
    hub = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = HubOverviewModel
        fields = (
            'hub',
            'image'
        )


class HubOverviewListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    serializer_class = HubOverviewModelSerializer
    queryset = HubOverviewModel.objects.all()

    def get_queryset(self):
        hub = shortcuts.get_object_or_404(HubModel, code=self.kwargs['hub_code'])
        return self.queryset.filter(hub=hub)

    def perform_create(self, serializer):
        hub = shortcuts.get_object_or_404(HubModel, code=self.kwargs['hub_code'])
        obj = serializer.save(hub=hub)
        hub.newest_overview = obj
        hub.save(update_fields=('newest_overview',))
        return obj


class HubOverviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HubOverviewModelSerializer
    queryset = HubOverviewModel.objects.all()

    def get_queryset(self):
        return self.queryset.filter(hub_id=self.kwargs['hub_pk'])

