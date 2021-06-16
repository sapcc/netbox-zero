from extras.plugins import PluginConfig

class NetboxZeroConfig(PluginConfig):
    name = 'netbox_zero'
    verbose_name = 'Netbox Zero'
    description = ''
    version = '0.8.0'
    author = 'Andrew Battye'
    author_email = 'andrew.battye@sap.com'
    base_url = 'netbox-zero'
    default_settings = {}
    caching_config = {
        '*': None
    }

config = NetboxZeroConfig
