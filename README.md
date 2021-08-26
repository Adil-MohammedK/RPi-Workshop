# RPI Workshop

This readme is made as reference for the session

### Using SSH

To use SSH, Download PuTTY or use WSL in WIndows. For Linux, use command:  
`ssh pi@raspberrypi.local`  
and then login using the password.

To install WSL: [Go Here](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

## Softwares to Install

- Python:
   <pre><code>sudo apt install python3</code></pre>
- Git:
   <pre><code>sudo apt install git</code></pre>
- Pip:
   <pre><code>sudo apt install python3-pip</code></pre>

### Python Libraries

- Py-Serial:
  <pre><code>pip3 install pyserial</code></pre>
- nrf24:
  <pre><code>pip3 install nrf24</code></pre>

To make python file, type:

<pre><code>nano filename.py</code></pre>

To run python program, type:

<pre><code>python3 filename.py</code></pre>

## Intro to IOT

1. We will be using IOTstack. So Firstly update and upgrade your s ystem.

   <pre><code>sudo apt update
   sudo apt upgrade -y</code></pre>

   Before we install IOTstack, we install dependencies of Hassio,
   <pre><code>sudo apt install -y apparmor apparmor-profiles apparmor-utils
   sudo apt install -y software-properties-common apt-transport-https ca-certificates dbus</code></pre>

   Install Network-Manager
   <pre><code>sudo apt install -y network-manager</code></pre>

2. To install IOTstack
   <pre><code>curl -fsSL https://raw.githubusercontent.com/SensorsIot/IOTstack/master/install.sh | bash</code></pre>

   And then reboot the system.

3. Run the menu and choose your containers:
   <pre><code>cd ~/IOTstack
   ./menu.sh</code></pre>
4. Bring up your stack:
   <pre><code>docker-compose up -d</code></pre>

### Installing Hassio Supervised

To install Home Assistant Supervised, open Menu using

<pre><code>sudo ./menu.sh</code></pre>

Select Native Installs and then select Hassio.  
In the menu listing out the device to install, select required Raspberry Pi Model or use qemux86-64 if using on PC. Type 'y' wherever required to confirm.  
Wait for some minutes until it installs.

Check your ip address using

<pre><code>sudo ifconfig</code></pre>

Note down the ip address.

Now go to a browser and type `ipaddress:8123` as the URL. Finish out the following data.

Install ESPHome from Add on store. Open ESPHome menu from supervisor. Turn it on.

Then create a new device by pressing the + button. Type necessary details and select type of device. Once new device is created, press Install on it and the select Manual. Downlaod the .bin file. Install Tasmotizer from
[Link](https://github.com/tasmota/tasmotizer/releases/).

Use Tasmotizer to write the image to ESP device by conncting it to PC via USB cable.

# Media Server

We will be installing:

- Plex
- Sonarr
- Radarr
- Bazarr
- Jackett
- Transmission
- Samba

### Installing Samba

1. <pre><code>sudo apt-get install samba samba-common-bin</code></pre>
2. Create shared folder
   <pre><code>mkdir /home/pi/shared</code></pre>
3. Edit Config file
   <pre><code>sudo nano /etc/samba/smb.conf</code></pre>
4. At the end of the file add the following
   <pre><code>[myShare]
   path = /home/pi/shared
   writeable=Yes
   create mask=0777
   directory mask=0777
   public=no</code></pre>
5. Save the file
6. Next, we need to set up a user for our Samba share on the Raspberry Pi
   <pre><code>sudo smbpasswd -a pi</code></pre>
   Enter password to use
7. <pre><code>sudo systemctl restart smbd</code></pre>
8. Get local ip address
   <pre><code>hostname -I</code></pre>
9. To connect to your Samba on Windows, begin by opening up the “File Explorer“.

   Within the “File Explorer” click the “Computer” tab (1.) then click “Map network drive”.  
   Within the “Folder” textbox (1.) you will want to enter the following “\\\raspberrypi\myShare.  
   Once done, click the “Finish” button to finalize the connection.  
   Finally, you will be asked to enter your login details to be able to finish the connection.

   Enter the username and password (1.) you set using the “smbpasswd” tool earlier on in the tutorial.

   Once done, press the “OK” button (2.) to continue.

## Downloading docker-compose for Server

1. Clone Server Repo
   <pre><code>git clone https://github.com/Adil-MohammedK/RPi-Media-Server.git</code></pre>
2. <pre><code>cd RPi-Media-Server</code></pre>
3. <pre><code>mv docker-compose.yml.bak docker-compose.yml</code></pre>
4. Make necessary changes to compose file
5. <pre><code>docker-compose up -d</code></pre>
6. Find rest of set up at our Youtube Video

# Blutooth Speaker

Type the following

<pre><code>sudo -i
bash <(curl -s https://raw.githubusercontent.com/lukasjapan/bt-speaker/master/install.sh)</code></pre>

Depending on your application, you might also want to send all audio to the headphone jack. This can be done by `raspi-config`:

`Advanced Options` -> `Audio` -> `Force 3.5mm ('headphone') jack`

Note: Bt-speaker has been made with the default Raspberry Pi OS audio configuration in mind. If you are using external sound cards or have installed a sound daemon (like PulseAudio or Jack) you might need to adjust the config file accordingly.

## Airplay Speaker

Create docker-compose file and build it.

<pre><code>
version: '3.3'
services:
    shairport-sync:
        container_name: shairplay
        restart: unless-stopped
        network_mode: host
        devices:
            - /dev/snd
        image: mikebrady/shairport-sync
        volumes:
            - /etc/shairport-sync.conf:/etc/shairport-sync.conf
</code></pre>
