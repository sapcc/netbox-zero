from extras.plugins import PluginTemplateExtension


class SiteTopologyButtons(PluginTemplateExtension):
    """
    Extend the DCIM site template to include content from this plugin.
    """
    model = 'dcim.site'

    def buttons(self):
        return self.render('netbox_zero/site_topo_button.html')


# PluginTemplateExtension subclasses must be packaged into an iterable named
# template_extensions to be imported by NetBox.
template_extensions = [SiteTopologyButtons]
