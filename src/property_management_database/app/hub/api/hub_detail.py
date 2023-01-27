from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import serializers
from rest_framework import permissions
from rest_framework import exceptions
from django_filters import rest_framework as drf_filter
import shortuuid
from ..models import HubModel, LocationModel

from .hub import HubSerializer


class HubDetailRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = HubSerializer
    queryset = HubModel.objects.all()

    def get_object(self):
        return get_object_or_404(HubModel, code=self.kwargs['hub_code'])
