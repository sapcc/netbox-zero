import json

from rest_framework.viewsets import ViewSetMixin
from dcim.models.devices import Device
from .dispatcher import ViewFactory
from rest_framework import generics
from rest_framework.response import Response
from django.http.response import HttpResponse
import json as j
from django.http import JsonResponse
from django.utils.decorators import classonlymethod
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView

from rest_framework.utils import json

from .platform.error import ErrorViewSet
from .utils import Anonymous,DeviceJson
from .serializers import DeviceSerializer
from .utils  import JSONRenderer



class ZtpMixin(ViewSetMixin):
    @classonlymethod
    def as_view(cls, actions=None, **initkwargs):


        def view(request, *args, **kwargs):
            viewfactory = ViewFactory()
            view = viewfactory.get_view(request,**initkwargs)
            self = view
            if self is None:
                self =  ErrorViewSet(status=404, **initkwargs)
            self.action_map = actions

            for method, action in actions.items():
                handler = getattr(self, action)
                setattr(self, method, handler)

            return self.dispatch(request, *args, **kwargs)
        return csrf_exempt(view)

class DeviceJSONViewSet(ViewSetMixin, generics.GenericAPIView):

    queryset = Device.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = DeviceSerializer
    permission_classes = [Anonymous]


    def list(self, request):

        device = request.query_params["device"]
        if device is not None:
            devices = self.get_by_serial(device)

        if devices.first() is None:
            devices = self.get_by_id(device)


        if devices.first() is None:
            response =  Response( template_name="404.html",content_type='text/json')
            response.status_code = 404
            return response

        res = DeviceJson(DeviceSerializer(devices.first(), many=False,context={'request': request}).data).dumps()

        response =  JsonResponse(res,safe=False)


        return response


    def get_by_serial(self, serial):
        devices = Device.objects.prefetch_related('interfaces').filter(serial=serial)
        return devices

    def get_by_id(self, id):
        devices = Device.objects.prefetch_related('interfaces').filter(id=id)
        return devices


class DispatcherViewSet(ZtpMixin, generics.GenericAPIView):
    queryset = Device.objects.all()



    def list(self, request):
        pass

