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
   <pre><code>sudo vi /etc/NetworkManager/NetworkManager.conf</code></pre>

2. To install IOTstack
   <pre><code>curl -fsSL https://raw.githubusercontent.com/SensorsIot/IOTstack/master/install.sh | bash</code></pre>

   And then reboot the system.

3. Run the menu and choose your containers:
   <pre><code>cd ~/IOTstack
   ./menu.sh</code></pre>
4. Bring up your stack:
   <pre><code>docker-compose up -d</code></pre>
