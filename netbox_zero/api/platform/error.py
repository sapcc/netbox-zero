
from dcim.models.devices import Device
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .. import serializers
from ..utils import Anonymous
from ..utils  import ZTPTextRenderer

class ErrorViewSet(GenericViewSet):

    queryset = Device.objects.all()
    renderer_classes = [ZTPTextRenderer]
    template_name = 'netbox_zero/api/{}.txt'
    # serializer_class = serializers.DeviceSerializer
    # permission_classes = [Anonymous]

    def __init__(self, status=200,**initkwargs):
        super().__init__(**initkwargs)
        self.status = status

    def list(self, request):
        response =  Response( template_name=self.template_name.format(self.status),content_type='text/plain',status=self.status)

        return response


