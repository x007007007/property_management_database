from django.urls import (
    path,
)
from . import api


urlpatterns = [
    path('hub/', api.hub.HubListCreateAPIView.as_view()),
    path('hub/<int:pk>/', api.hub.HubRetrieveUpdateDestroyAPIView.as_view()),
    path('hub/<int:pk>/qrcode/', api.hub_qr_code.HubQRCodeView.as_view()),
    path('hub/<int:hub_pk>/photo/', api.photo.HubOverviewListCreateAPIView.as_view()),
]