from dcim.models import Device, Site, Region
from django import forms
from utilities.forms import (
    BootstrapMixin, DynamicModelMultipleChoiceField,
)


class TopologyFilterForm(BootstrapMixin, forms.Form):

    model = Device

    device_id = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
    )
    site_id = DynamicModelMultipleChoiceField(
        queryset=Site.objects.all(),
        required=False,
        to_field_name='id',
        null_option='None',
    )
    region_id = DynamicModelMultipleChoiceField(
        queryset=Region.objects.all(),
        required=False,
        to_field_name='id',
        null_option='None',
    )


