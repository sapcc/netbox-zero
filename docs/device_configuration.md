# Device configuration
Netbox Zero responds to the bootfile HTTP request with a 
text file containing device platform specifc content determined 
for the specfiied device, HTTP headers are used to determine the 
platform and device see [architecture](architecture.md) and [supported platforms](supported_platforms.md).

Th configuration can be accessed at `https://[netbox ip/fqdn]/api/plugins/netbox-zero/ztp/`, the required 
HTTP headers for each plaform are required. This configutation 
is generated by applying a serialized version of the device
to a Django template. 

You can also access the serialized content directly in json form
at `"https://[netbox ip/fqdn]/api/plugins/netbox-zero/json?device=[device_id]"` 
the parameter device is the device specific identifier e.g. serial number or macacddress

The following devices are available :
* [Arista EOS](platform/eos.md)
* [Arista vEOS](platform/veos.md)
* [Cisco IOS XE](platform/todo.md)

A example serilized device response, in json format,  is shown below in JSON 
format and all values should be avaiable for use in 
configuration Django templates either directly or via an embeded object. 

<pre>
  "id": 15217,
  "url": "http://localhost:8000/api/dcim/devices/15217/",
  "display": "qa-de-6-sw2100c",
  "name": "qa-de-6-sw2100c",
  "display_name": "qa-de-6-sw2100c",
  "device_type": {
    "id": 144,
{
    "url": "http://localhost:8000/api/dcim/device-types/144/",
    "display": "DCS 7280CR3-32P4",
    "manufacturer": {
      "id": 6,
      "url": "http://localhost:8000/api/dcim/manufacturers/6/",
      "display": "Arista",
      "name": "Arista",
      "slug": "arista"
    },
    "model": "DCS 7280CR3-32P4",
    "slug": "7280cc3-32p4",
    "display_name": "Arista DCS 7280CR3-32P4"
  },
  "device_role": {
    "id": 38,
    "url": "http://localhost:8000/api/dcim/device-roles/38/",
    "display": "EVPN Spine",
    "name": "EVPN Spine",
    "slug": "evpn-spine"
  },
  "tenant": {
    "id": 1,
    "url": "http://localhost:8000/api/tenancy/tenants/1/",
    "display": "Converged Cloud",
    "name": "Converged Cloud",
    "slug": "converged-cloud"
  },
  "platform": null,
  "serial": "52:54:00:2f:3d:35",
  "asset_tag": null,
  "site": {
    "id": 38,
    "url": "http://localhost:8000/api/dcim/sites/38/",
    "display": "QA-DE-6a",
    "name": "QA-DE-6a",
    "slug": "qa-de-6a"
  },
  "location": null,
  "rack": null,
  "position": null,
  "face": null,
  "parent_device": null,
  "status": {
    "value": "active",
    "label": "Active"
  },
  "primary_ip": {
    "id": 51574,
    "url": "http://localhost:8000/api/ipam/ip-addresses/51574/",
    "display": "10.246.3.94/26",
    "family": 4,
    "address": "10.246.3.94/26"
  },
  "primary_ip4": {
    "id": 51574,
    "url": "http://localhost:8000/api/ipam/ip-addresses/51574/",
    "display": "10.246.3.94/26",
    "family": 4,
    "address": "10.246.3.94/26"
  },
  "primary_ip6": null,
  "cluster": null,
  "virtual_chassis": null,
  "vc_position": null,
  "vc_priority": null,
  "comments": "",
  "local_context_data": null,
  "custom_fields": {
    "DC Label": ""
  },
  "created": "2021-06-01",
  "last_updated": "2021-06-01T09:24:02.400490Z",
  "config_context": {
    "cc": {
      "net": {
        "service": {
          "dns": [
            "147.204.9.200",
            "147.204.9.201"
          ],
          "ntp": [
            {
              "ip": "147.204.9.202",
              "name": "timehost1.global.cloud.sap"
            },
            {
              "ip": "147.204.9.203",
              "name": "timehost2.global.cloud.sap"
            },
            {
              "ip": "147.204.9.204",
              "name": "timehost3.global.cloud.sap"
            }
          ],
          "ldap": [
            "ldap.global.cloud.sap"
          ],
          "syslog": []
        },
        "vpn_asn": 65126
      },
      "region_id_table": {
        "af-za-1": 19,
        "ap-ae-1": 9,
        "ap-au-1": 10,
        "ap-cn-1": 11,
        "ap-in-1": 18,
        "ap-jp-1": 12,
        "ap-jp-2": 13,
        "ap-sa-1": 14,
        "ap-sg-1": 15,
        "eu-de-1": 1,
        "eu-de-2": 2,
        "eu-nl-1": 3,
        "eu-ru-1": 4,
        "la-br-1": 17,
        "na-ca-1": 5,
        "na-us-1": 6,
        "na-us-2": 7,
        "na-us-3": 8,
        "qa-de-1": 16
      },
      "boot": {
        "iso": "https://repo.eu-nl-1.cloud.sap/vmware-binaries/cc-prod-binaries/vmware/VMware_ESXi_6.7.0_16316930_Custom_DellEMC_v1.4_SAP_unattended.iso"
      }
    },
    "vpod": {
      "datastores": {
        "vmfs": {
          "eph": [
            {
              "name": "eph-bb232-6",
              "type": "VMFS",
              "capacity": 16492405981184
            },
            {
              "name": "eph-bb232-3",
              "type": "VMFS",
              "capacity": 16492405981184
            },
            {
              "name": "eph-bb232-4",
              "type": "VMFS",
              "capacity": 16492405981184
            },
            {
              "name": "eph-bb232-2",
              "type": "VMFS",
              "capacity": 16492405981184
            },
            {
              "name": "eph-bb232-5",
              "type": "VMFS",
              "capacity": 16492405981184
            },
            {
              "name": "eph-bb232-1",
              "type": "VMFS",
              "capacity": 16492405981184
            }
          ],
          "management": [
            {
              "name": "BB232_Management_DS03",
              "type": "VMFS",
              "capacity": 1099243192320
            },
            {
              "name": "BB232_Management_DS02",
              "type": "VMFS",
              "capacity": 1099243192320
            },
            {
              "name": "BB232_Management_DS01",
              "type": "VMFS",
              "capacity": 1099243192320
            }
          ]
        },
        "vvol": {
          "cinder": ""
        }
      }
    }
  },
  "ntp_servers": [
    "147.204.9.202",
    "147.204.9.203",
    "147.204.9.204"
  ],
  "interface_set": [
    {
      "id": 299747,
      "url": "http://localhost:8000/api/dcim/interfaces/299747/",
      "display": "Ethernet1/1",
      "device": 15217,
      "name": "Ethernet1/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.611451Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299748,
      "url": "http://localhost:8000/api/dcim/interfaces/299748/",
      "display": "Ethernet2/1",
      "device": 15217,
      "name": "Ethernet2/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612007Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299749,
      "url": "http://localhost:8000/api/dcim/interfaces/299749/",
      "display": "Ethernet3/1",
      "device": 15217,
      "name": "Ethernet3/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612076Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299750,
      "url": "http://localhost:8000/api/dcim/interfaces/299750/",
      "display": "Ethernet4/1",
      "device": 15217,
      "name": "Ethernet4/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612137Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299751,
      "url": "http://localhost:8000/api/dcim/interfaces/299751/",
      "display": "Ethernet5/1",
      "device": 15217,
      "name": "Ethernet5/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612195Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299752,
      "url": "http://localhost:8000/api/dcim/interfaces/299752/",
      "display": "Ethernet6/1",
      "device": 15217,
      "name": "Ethernet6/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612252Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299753,
      "url": "http://localhost:8000/api/dcim/interfaces/299753/",
      "display": "Ethernet7/1",
      "device": 15217,
      "name": "Ethernet7/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612308Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299754,
      "url": "http://localhost:8000/api/dcim/interfaces/299754/",
      "display": "Ethernet8/1",
      "device": 15217,
      "name": "Ethernet8/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612365Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299755,
      "url": "http://localhost:8000/api/dcim/interfaces/299755/",
      "display": "Ethernet9/1",
      "device": 15217,
      "name": "Ethernet9/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612421Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299756,
      "url": "http://localhost:8000/api/dcim/interfaces/299756/",
      "display": "Ethernet10/1",
      "device": 15217,
      "name": "Ethernet10/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612477Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299757,
      "url": "http://localhost:8000/api/dcim/interfaces/299757/",
      "display": "Ethernet11/1",
      "device": 15217,
      "name": "Ethernet11/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612533Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299758,
      "url": "http://localhost:8000/api/dcim/interfaces/299758/",
      "display": "Ethernet12/1",
      "device": 15217,
      "name": "Ethernet12/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612589Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299759,
      "url": "http://localhost:8000/api/dcim/interfaces/299759/",
      "display": "Ethernet13/1",
      "device": 15217,
      "name": "Ethernet13/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612645Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299760,
      "url": "http://localhost:8000/api/dcim/interfaces/299760/",
      "display": "Ethernet14/1",
      "device": 15217,
      "name": "Ethernet14/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612701Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299761,
      "url": "http://localhost:8000/api/dcim/interfaces/299761/",
      "display": "Ethernet15/1",
      "device": 15217,
      "name": "Ethernet15/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612757Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299762,
      "url": "http://localhost:8000/api/dcim/interfaces/299762/",
      "display": "Ethernet16/1",
      "device": 15217,
      "name": "Ethernet16/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612813Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299763,
      "url": "http://localhost:8000/api/dcim/interfaces/299763/",
      "display": "Ethernet17/1",
      "device": 15217,
      "name": "Ethernet17/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612869Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299764,
      "url": "http://localhost:8000/api/dcim/interfaces/299764/",
      "display": "Ethernet18/1",
      "device": 15217,
      "name": "Ethernet18/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.612947Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299765,
      "url": "http://localhost:8000/api/dcim/interfaces/299765/",
      "display": "Ethernet19/1",
      "device": 15217,
      "name": "Ethernet19/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.613036Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299766,
      "url": "http://localhost:8000/api/dcim/interfaces/299766/",
      "display": "Ethernet20/1",
      "device": 15217,
      "name": "Ethernet20/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.613174Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299767,
      "url": "http://localhost:8000/api/dcim/interfaces/299767/",
      "display": "Ethernet21/1",
      "device": 15217,
      "name": "Ethernet21/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.613230Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299768,
      "url": "http://localhost:8000/api/dcim/interfaces/299768/",
      "display": "Ethernet22/1",
      "device": 15217,
      "name": "Ethernet22/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.613286Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299769,
      "url": "http://localhost:8000/api/dcim/interfaces/299769/",
      "display": "Ethernet23/1",
      "device": 15217,
      "name": "Ethernet23/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.613342Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299770,
      "url": "http://localhost:8000/api/dcim/interfaces/299770/",
      "display": "Ethernet24/1",
      "device": 15217,
      "name": "Ethernet24/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.613397Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299771,
      "url": "http://localhost:8000/api/dcim/interfaces/299771/",
      "display": "Ethernet25/1",
      "device": 15217,
      "name": "Ethernet25/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.613453Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299772,
      "url": "http://localhost:8000/api/dcim/interfaces/299772/",
      "display": "Ethernet26/1",
      "device": 15217,
      "name": "Ethernet26/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.613509Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299773,
      "url": "http://localhost:8000/api/dcim/interfaces/299773/",
      "display": "Ethernet27/1",
      "device": 15217,
      "name": "Ethernet27/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.613565Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299774,
      "url": "http://localhost:8000/api/dcim/interfaces/299774/",
      "display": "Ethernet28/1",
      "device": 15217,
      "name": "Ethernet28/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.613621Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299775,
      "url": "http://localhost:8000/api/dcim/interfaces/299775/",
      "display": "Ethernet29/1",
      "device": 15217,
      "name": "Ethernet29/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.613677Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299776,
      "url": "http://localhost:8000/api/dcim/interfaces/299776/",
      "display": "Ethernet30/1",
      "device": 15217,
      "name": "Ethernet30/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.613733Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299777,
      "url": "http://localhost:8000/api/dcim/interfaces/299777/",
      "display": "Ethernet31/1",
      "device": 15217,
      "name": "Ethernet31/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.613819Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299778,
      "url": "http://localhost:8000/api/dcim/interfaces/299778/",
      "display": "Ethernet32/1",
      "device": 15217,
      "name": "Ethernet32/1",
      "label": "",
      "type": "100gbase-x-qsfp28",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.613929Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299779,
      "url": "http://localhost:8000/api/dcim/interfaces/299779/",
      "display": "Ethernet33/1",
      "device": 15217,
      "name": "Ethernet33/1",
      "label": "",
      "type": "400gbase-x-osfp",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.613985Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299780,
      "url": "http://localhost:8000/api/dcim/interfaces/299780/",
      "display": "Ethernet34/1",
      "device": 15217,
      "name": "Ethernet34/1",
      "label": "",
      "type": "400gbase-x-osfp",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.614040Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299781,
      "url": "http://localhost:8000/api/dcim/interfaces/299781/",
      "display": "Ethernet35/1",
      "device": 15217,
      "name": "Ethernet35/1",
      "label": "",
      "type": "400gbase-x-osfp",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.614095Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299782,
      "url": "http://localhost:8000/api/dcim/interfaces/299782/",
      "display": "Ethernet36/1",
      "device": 15217,
      "name": "Ethernet36/1",
      "label": "",
      "type": "400gbase-x-osfp",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.614150Z",
      "count_ipaddresses": 0,
      "_occupied": false,
      "ip_addresses_set": [],
      "primary_ip": null,
      "primary_vrf": null,
      "router": null
    },
    {
      "id": 299783,
      "url": "http://localhost:8000/api/dcim/interfaces/299783/",
      "display": "Management1",
      "device": 15217,
      "name": "Management1",
      "label": "",
      "type": "1000base-t",
      "enabled": true,
      "parent": null,
      "lag": null,
      "mtu": null,
      "mac_address": null,
      "mgmt_only": false,
      "description": "",
      "mode": "",
      "untagged_vlan": null,
      "tagged_vlans": [],
      "mark_connected": false,
      "cable": null,
      "created": "2021-06-01",
      "last_updated": "2021-06-01T09:20:43.614206Z",
      "count_ipaddresses": 1,
      "_occupied": false,
      "ip_addresses_set": [
        {
          "id": 51574,
          "display": "10.246.3.94/26",
          "family": 4,
          "address": "10.246.3.94/26",
          "vrf": 1,
          "tenant": null,
          "status": "active",
          "role": "",
          "assigned_object_type": 26,
          "assigned_object_id": 299783,
          "nat_inside": null,
          "nat_outside": null,
          "dns_name": "",
          "description": "",
          "created": "2021-06-01",
          "last_updated": "2021-06-01T09:22:57.010951Z"
        }
      ],
      "primary_vrf": "CC-MGMT"
    }
  ]
}
</pre>
    

