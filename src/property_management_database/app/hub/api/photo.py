from rest_framework import generics
from rest_framework import serializers
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
    serializer_class = HubOverviewModelSerializer
    queryset = HubOverviewModel.objects.all()

    def get_queryset(self):
        hub = HubModel.objects.get(id=self.kwargs['hub_pk'])
        return self.queryset.filter(hub=hub)

    def perform_create(self, serializer):
        hub = HubModel.objects.get(id=self.kwargs['hub_pk'])
        return serializer.save(hub=hub)


class HubOverviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HubOverviewModelSerializer
    queryset = HubOverviewModel.objects.all()

    def get_queryset(self):
        return self.queryset.filter(hub_id=self.kwargs['hub_pk'])

