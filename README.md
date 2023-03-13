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
<br />
Controller 3: `172.16.1.7`
<br /><br />
Ports:
<br />
GUI: `8181`
<br />
CLI: `8101`
<br />
OpenFlow: `6653`
<br /><br />

**Using the hosts public IP:**
<br />
Acess the three controllers GUIs at:
<br />
Controller 1: `http://IP:8181/onos/ui`
<br />
Controller 2: `http://IP:8182/onos/ui`
<br />
Controller 3: `http://IP:8183/onos/ui`
<br /><br />
CLI Ports:
<br />
Controller 1: `8101`
<br />
Controller 2: `8102`
<br />
Controller 3: `8103`
<br /><br />
OpenFlow ports:
<br />
Controller 1: `6653`
<br />
Controller 2: `6654`
<br />
Controller 3: `6655`
<br /><br />

**To connect to ONOS CLI:**
<br />
Command: `ssh -p PORT karaf@IP`
<br />
Example: `ssh -p 8101 karaf@192.168.5.4`
<br />
Password: `karaf`
<br />

**To acess the Mininet container created in the compose file:**
<br />
`sudo docker exec -it mininet bash`
<br />
Once inside the continer run your Mininet command.
<br />
Mininet command cluster example:
<br />
`mn --controller remote,ip=IP,port=6653 --controller remote,ip=IP,port=6654 --controller remote,ip=IP,port=6655 --topo tree,3`
<br /><br />

ovs−vsctl − − set Bridge s1 ipfix=@i −− −−id=@i create IPFIX targets=\”192.168.2.249:2055\” obs_domain_id=123 obs_point_id=456
<br />
./goflow2-1.1.1-linux-x86_64 -format.selector SrcAddr,DstAddr,SrcMac,DstMac,InIf,OutIf,SrcPort,DstPort -transport.file meeting.json



updated goflow2 command (this command will enable kafka and send output in protobuf for topic named flows)

./goflow2 -transport=kafka -transport.kafka.brokers=localhost:9092 -transport.kafka.topic=flows -format=pb -format.selector SrcAddr,DstAddr,SrcMac,DstMac,InIf,OutIf,SrcPort,DstPort,ObservationPointID,ObservationDomainID,SequenceNum,TimeFlowStart,TimeFlowEnd

