from rest_framework import generics
from rest_framework import serializers
from rest_framework import permissions
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


class HubListFilterSet(drf_filter.FilterSet):
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
