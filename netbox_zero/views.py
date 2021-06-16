from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin

class RootView(PermissionRequiredMixin, View):
    """Generic Topology View"""
    permission_required = ('dcim.view_site', 'dcim.view_device', 'dcim.view_cable')
    # queryset = Device.objects.all()
    # filterset = filters.TopologyFilterSet
    template_name = 'netbox_zero/root.html'

    def get(self, request):

        return render(request, self.template_name, {
                'requestGET': dict(request.GET),
        })


class SiteTopologyView(RootView):
    template_name = 'netbox_zero/site_topology.html'
