import codecs
from django.utils.encoding import smart_text
from rest_framework.permissions import BasePermission
from rest_framework.renderers import BaseRenderer
from rest_framework.renderers import TemplateHTMLRenderer

import json as j
from django.db import models
from collections import OrderedDict
from django.forms.boundfield import BoundField


from dcim.models.device_components import Interface

class ZTPTextRenderer(TemplateHTMLRenderer):
    media_type = 'text/plain'
    format = 'text'
    charset = 'utf-8'

class JSONRenderer(BaseRenderer):
    media_type = 'text/json'
    format = 'text'
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        orig  = DeviceJson(data)
        return orig.dumps(indent=2)




class Anonymous(BasePermission):
    """
    Returns True
    """
    def has_permission(self, request, view):
        return True

class DeviceJson:
    def __init__(self,data):
        self.data  = data

    def dumps(self,indent=0):
        dict ={}

        if not hasattr(self.data,"keys"):
            dict = self.data
        else:
            for k in self.data.keys():
                if isinstance(self.data[k],BoundField):
                    dict[k] = self.data[k].value()
                if isinstance(self.data[k],list):
                    result = []
                    for sub in self.data[k]:
                        result.append(DeviceJson(sub).dumps())

                    dict[k] =result
                elif isinstance(self.data[k],OrderedDict):
                    json = DeviceJson( self.data[k])
                    dict[k]= json.dumps()

                elif isinstance(self.data[k],Interface):
                    json = DeviceJson( self.data[k])
                    dict[k]= json.dumps()

                else:
                    if(hasattr(self.data[k],"value")):
                        if callable(self.data[k]):
                            dict[k] = self.data[k].value()
                    else:
                        dict[k] = self.data[k]

                res = str(dict).replace("\\'","")
                res = res.replace("'","\"")
                res = res.replace("None","\"null\"")
                res = res.replace("False","\"false\"")
                res = res.replace("True","\"true\"")

                res = eval(res)

        return dict