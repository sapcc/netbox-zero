# Installing the Netbox-Zero Plugin

Its easiest if Netbox is be running locally in 
development mode using the instructions 
[here](https://netbox.readthedocs.io/en/stable/installation/3-netbox/). In the Netbox section follow **Option B: Clone the Git Repository** and clone netbox into [netbox root].

#### In the locally cloned Netbox repository
Ensure the plugin is active in Netbox configuration.py

    ../netbox/netbox/configuration.py

Activate the netbox-zero plugin by adding it to list of
active plugins.

    PLUGINS = ['netbox_zero']

Restart the Netbox server process.

#### Clone the netbox-zero repository

    mkdir [netbox-zero root]
    cd [netbox-zero root]
    git clone -b master https://github.com/sapcc/netbox-zero.git

#### Activate the netbox venv

From the local repository directory activate the core 
Netbox virtual environment) venv.  

    cd  [netbox-zero root]/netbox-zero
    netbox-zero > source [netbox root]/netbox/venv/bin/activate

#### Install the plugin into the core Netbox application

    netbox-zero > python3 setup.py develop


After install restart Netbox.

Netbox will also intermittently restart on changes, however 
note that all changes arenot always detected. In general  
changes to the E.g. It will generally restart when plugin 
file changes are detected, but when multiple changes are 
made or several files are added or removed this may not 
happens. 

#### Check Plugin installation activation
You can check the plugin is activa and installaed by 
logging into Netbox. In the top level menu click on 
*Plugins* and in the drop down you should see *Netbox Zero*
in the list. The API should now be accessible at 
[http://localhost:8000/api/plugins/netbox-zero/ztp/](http://localhost:8000/api/plugins/netbox-zero/ztp/). 
You should be able to test it be settings the required 
HTTP headers.