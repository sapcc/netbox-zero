import time
from dcim.models.devices import Device
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .. import serializers
from ..utils import Anonymous
from ..utils  import ZTPTextRenderer


class EOSViewSet(GenericViewSet):

    queryset = Device.objects.all()
    renderer_classes = [ZTPTextRenderer]
    template_name = 'netbox_zero/api/eos.txt'
    serializer_class = serializers.DeviceSerializer
    permission_classes = [Anonymous]

    def use_for_request(self,request):
        return request.META.get("HTTP_X_ARISTA_MODELNAME")=="vEOS"


    def list(self, request):

        serial = request.META.get('HTTP_X_ARISTA_SERIAL')
        if serial is not None:
            device = self.get_by_serial(serial)
        else :
            serial  = request.META.get('HTTP_X_ARISTA_SYSTEMMAC')
            device = self.get_by_serial(serial)



        if device is None:
            response =  Response( template_name='netbox_zero/api/404.txt',content_type='text/plain',status=404)
            return response

        response =  Response( template_name=self.template_name,content_type='text/plain')
        response.data=self.get_serializer(device, many=False).data


        return response


    def get_by_serial(self, serial):
        device = Device.objects.prefetch_related('interfaces').get(serial=serial)


        return device