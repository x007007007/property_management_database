from rest_framework import generics
from rest_framework import serializers
import shortuuid
from ..models import HubModel


class HubSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source="newest_overview.image", default=None, read_only=True)
    code = serializers.CharField(read_only=True)

    class Meta:
        model = HubModel
        fields = (
            'name',
            'code',
            'image',
            'location',
        )


class HubListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = HubSerializer
    queryset = HubModel.objects.all()

    def perform_create(self, serializer):
        while True:
            code = shortuuid.ShortUUID().random(length=6)
            if HubModel.objects.filter(code=code).count() == 0:
                break
        serializer.save(code=code)


class HubRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HubSerializer
    queryset = HubModel.objects.all()
