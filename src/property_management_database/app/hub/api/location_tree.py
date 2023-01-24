from rest_framework import serializers
from rest_framework import generics

from ..models import LocationModel


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class LocationModelSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = LocationModel
        fields = (
            'id',
            'name',
            'children',
        )


class LocationRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LocationModelSerializer
    queryset = LocationModel.objects.all()

    def get_object(self):
        return self.get_queryset().filter(parent__isnull=True).first()


