from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import serializers
from rest_framework import permissions
from rest_framework import exceptions
from django_filters import rest_framework as drf_filter
import shortuuid
from ..models import HubModel, LocationModel


class HubLocationDetailSerializer(serializers.ModelSerializer):
    path = serializers.CharField(source="get_path")

    class Meta:
        model = LocationModel
        fields = (
            'id',
            'path'
        )


class HubSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source="newest_overview.image", default=None, read_only=True)
    code = serializers.CharField(read_only=True)
    location_detail = HubLocationDetailSerializer(source="location", read_only=True)

    class Meta:
        model = HubModel
        fields = (
            'id',
            'name',
            'code',
            'image',
            'location',
            'location_detail',
        )


class LocationFilter(drf_filter.Filter):
    def filter(self, qs, value):
        if (loc := LocationModel.objects.filter(id=value).first()) is None:
            return qs.none()
        assert isinstance(loc, LocationModel)
        children_pk = list(loc.get_leafnodes().values_list("pk", flat=True))
        children_pk.insert(0, value)
        return qs.filter(location__pk__in=children_pk)


class HubListFilterSet(drf_filter.FilterSet):
    location = LocationFilter()

    class Meta:
        model = HubModel
        fields = [
            'location',
        ]


class HubListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = HubSerializer
    permission_classes = [permissions.AllowAny]
    filterset_class = HubListFilterSet
    filter_backends = [drf_filter.DjangoFilterBackend]
    queryset = HubModel.objects.select_related('location').all()

    def perform_create(self, serializer):
        while True:
            code = shortuuid.ShortUUID().random(length=6)
            if HubModel.objects.filter(code=code).count() == 0:
                break
        serializer.save(code=code)


class HubRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HubSerializer
    queryset = HubModel.objects.all()

    def get_object(self):
        if self.lookup_url_kwarg in self.kwargs:
            return super().get_object()
        elif 'hub_code' in self.kwargs:
            return get_object_or_404(HubModel, code=self.kwargs['hub_code'])
        else:
            raise exceptions.NotFound("no current params")