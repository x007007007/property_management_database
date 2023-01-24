from rest_framework import generics
from django.http import response
from ..models import HubModel
import qrcode
import io


class HubQRCodeView(generics.RetrieveAPIView):
    queryset = HubModel.objects.all()

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=2,
            border=0,
        )
        qr.add_data(f"http://qr.local/{obj.code}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        fp = io.BytesIO()
        img.save(fp)
        fp.seek(0)
        return response.FileResponse(fp, content_type="image/png")
