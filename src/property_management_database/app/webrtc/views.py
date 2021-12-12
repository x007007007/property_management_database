import logging
import os
import json
import uuid
from django.shortcuts import render

from rest_framework import (
    serializers
)
import asyncio
import requests

from django.conf import settings
from django.http.response import JsonResponse
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaBlackhole, MediaPlayer, MediaRecorder, MediaRelay

from .video_trans import VideoTransformTrack
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import time

relay = MediaRelay()

LOGGER = logging.getLogger(__name__)

pcs = set()


async def offer(request):
    await asyncio.sleep(0.5)
    print('down')
    if request.method != 'POST':
        return JsonResponse({"option": ["POST"]}, status=402)
    else:
        params = json.loads(request.body.decode("utf-8"))
        resp = requests.post("https://192.168.1.8/offer", json=params)
        ret = resp.json()
        JsonResponse(data=ret)


def index(request):
    return render(request, "pmdb_webrtc/index.html")