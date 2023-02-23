# ONOS cluster creation using a Docker compose file
This compose file also automaticlly enables OpenFlow in the ONOS cluster to allow connection to Mininet
<br /><br />

**Portainer for easy GUI managment of Docker conatiners:**
<br />
`docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest`
<br /><br />
Portainer Web Interface: `https://IP:9443`

<br /><br />
**Downloading & Installation**
<br />
Start at your home directory: `cd ~`
<br />
Download tarball: `wget https://github.com/nat0321/mininet/raw/main/atomix-cluster/atomix-cluster.tgz`
<br />
Extract tarball: `tar xvfz atomix-cluster.tgz`
<br />
Enter extracted folder: `cd atomix-cluster`
<br />
Create the cluster with: `sudo docker-compose up -d`
<br />
Confirm the containers are running with `Portainer web GUI` or `sudo docker ps`
<br />
7 Containers should be created by the compose file
<br /><br />
The controllers can be accessed two ways through their Docker local IP or the hosts public IP
<br /><br />

**To acess them via their Docker local IP use the IPs listed below:**
<br />
Controller 1: `172.16.1.5`
<br />
Controller 2: `172.16.1.6`
