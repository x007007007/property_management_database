from django.urls import (
    path,
)
from . import api


urlpatterns = [
    path('hub/', api.hub.HubListCreateAPIView.as_view()),
    path('hub/<int:pk>/', api.hub.HubRetrieveUpdateDestroyAPIView.as_view()),
    path('hub/code/<str:hub_code>/', api.hub_detail.HubDetailRetrieveAPIView.as_view()),
    path('hub/<int:pk>/qrcode/', api.hub_qr_code.HubQRCodeView.as_view()),
    path('hub/<str:hub_code>/photo/', api.photo.HubOverviewListCreateAPIView.as_view()),
    path('location_tree/', api.location_tree.LocationRetrieveAPIView.as_view()),
]