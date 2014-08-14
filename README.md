HoneyMalt
=========

HoneyMalt is a Maltego transform pack for the analysis (graphing) of Honeypots. Starting with Kippo (that uses MySQL) you can now export all that lovely SQL data and have your Maltego graphs displaying it (as long as your machine doesn't blow up trying).

I've tried to use as many native Maltego entities as possible so you can make use of the built-in transforms and because I'm lazy.. (not really..)

The following python modules are also required:

**canari (goes without saying)  
MySQL Python Connector (mysql_connector_python)  
Python Geoip (pygeoip)**  

**IMPORTANT**  
If you are remotely connnecting to your kippo mysql instance you will need to allow remote connections. You can do this by running the following command:  

`GRANT ALL ON kippo.* TO kippo@'IPADDR' IDENTIFIED BY 'Kippo-DB-Pass';`  

You will need to change the *IPADDR* and *Kippo-DB-Pass* to match your requirements.

To install the transform pack you need to do the following (make sure you have canari installed already and run Maltego at least once):

clone this repo  
`git clone https://github.com/catalyst256/HoneyMalt.git`  
change to the src directory  
`cd src/`  
`canari create-profile HoneyMalt -w [full path to src folder]`  
on my machine this is:  
`canari create-profile HoneyMalt -w /root/localTransforms/HoneyMalt/src`  

This will create a **HoneyMalt.mtz** file in the `src/` directory and a **HoneyMalt.conf** file

Within the HoneyMalt.conf file you will need to enter your Kippo MySQL details (username, password, database name) and you can also change the location to your GeoIP file.

Load Maltego and import the configuration file that was just created in the src folder.
You will have a number of new transforms, entities and a Maltego machine to use.

To use HoneyMalt the process is as follows:

1. Add the Kippo Honeypot entity into a new graph  
2. Change the default IP to your MySQL server IP (or hostname)  
3. Right click, Run Machine, HoneyMalt - Kippo (auto)  
4. Go get coffee  

The Maltego machine will run all the available transforms in order and should go nuts and pull out all the nice information from your MySQL Kippo database. 

If you just want to look for specific sessions relating to "Evil IPs", you can right click on the Kippo Honeypot entity and chose `HoneyMalt - Kippo: Search for Sessions by IP`. This will give you a popup box asking for an IP address which then will go look for any sessions that originated from that IP.

I'm going to add some more search stuff later and expand the Honeypots you can target. Anything I've missed give me a shout..

Enjoy!! (any issues raise a ticket on GitHub)
