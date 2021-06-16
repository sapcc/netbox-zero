# DHCP Example with dnsmasq

Network zero can be used with dnsmasq to provide a DHCP 
server which supports the initial configuration of a device. 

Below is an example, minimal, dhcp.conf that can be used 
in `/etc/dnsmasq.d/dhcp.conf`. It shows the configuration 
of DHCP option 67 only, other configutation needs to be 
adjusted for your own environment. 

    port=0
    
    # To enable dnsmasq's DHCP server functionality.
    dhcp-range=192.168.0.100,168.0.200,255.255.255.0,2h
    
    dhcp-option=option:bootfile-name,"https://[netbox ip/fqdn]/api/plugins/netbox-zero/ztp/"
    
    # Set gateway as Router. Following two lines are identical.
    #dhcp-option=option:router,192.168.0.1
    dhcp-option=3,192.168.0.1
    
    # Set DNS server as Router.
    dhcp-option=6,8.8.8.8

As described the HTTP request sent to the URL specified in the 
bootfile option must include one or more HTTP headers identifying the
platform e.g. `X-DEVICE-PLATFORM: IOSXE, X-DEVICE-PLATFORM_VERSION: 17.4.1` 
and on or more header that can be used to idientify the device 
in netbpx e.g `X-DEVICE-SERIAL: A12345B` or `X-DEVICE-MAX: 00:12:AA:BB:34:56:78`.

These are used in the dispatcher to determine the platform specific view
and the platform specfic view to determins the device to prepare the 
configuration for and the configuration template.