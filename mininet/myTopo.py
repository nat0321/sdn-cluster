from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.node import OVSKernelSwitch
from mininet.node import Host
from mininet.node import RemoteController
from mininet.util import quietRun
import time

def emptynet():

    # Creating empty network
    net = Mininet(controller=RemoteController, waitConnected=True)

    # Adding remote ONOS controller
    #c1 = net.addController('c1', controller=RemoteController, ip='172.16.235.233', port=6653) #problem here
    c1 = net.addController('c1', controller=RemoteController, ip='175.24.1.10', port=6653)
    c2 = net.addController('c2', controller=RemoteController, ip='175.24.1.10', port=6654)
    c3 = net.addController('c3', controller=RemoteController, ip='175.24.1.10', port=6655)



    # Adding Hosts
    host1 = net.addHost('host1', cls=Host, ip='10.0.0.6')
    host2 = net.addHost('host2', cls=Host, ip="10.0.0.7")
    host3 = net.addHost('host3', cls=Host, ip="10.0.0.8") 
    
    host4 = net.addHost('host4', cls=Host, ip='10.0.0.9')
    host5 = net.addHost('host5', cls=Host, ip="10.0.0.10")
    host6 = net.addHost('host6', cls=Host, ip="10.0.0.11") 
    
    host7 = net.addHost('host7', cls=Host, ip='10.0.0.12')
    host8 = net.addHost('host8', cls=Host, ip="10.0.0.13")
    host9 = net.addHost('host9', cls=Host, ip="10.0.0.14")
    
    host10 = net.addHost('host10', cls=Host, ip='10.0.0.15')
    host11 = net.addHost('host11', cls=Host, ip="10.0.0.16")
    host12 = net.addHost('host12', cls=Host, ip="10.0.0.17") 
    print ("Added hosts")


    # Adding Switches
    switch1 = net.addSwitch('s1', cls=OVSKernelSwitch, ip='10.0.0.22')
    switch2 = net.addSwitch('s2', cls=OVSKernelSwitch, ip='10.0.0.23')
    switch3 = net.addSwitch('s3', cls=OVSKernelSwitch, ip='10.0.0.24')
    switch4 = net.addSwitch('s4', cls=OVSKernelSwitch, ip='10.0.0.25')
    
    net.addLink(switch1, c1)
    net.addLink(switch2, c1)
    net.addLink(switch3, c1)
    net.addLink(switch4, c1)


    # Adding Links
    
    #connect switches
    net.addLink (switch1, switch2)
    net.addLink (switch2, switch3)
    net.addLink (switch3, switch4)

    
    net.addLink(switch1, host1)
        
    net.addLink(switch1, host2)
    net.addLink(switch1, host3)

    net.addLink(switch2, host4)
    net.addLink(switch2, host5)
    net.addLink(switch2, host6)
    
    net.addLink(switch3, host7)
    net.addLink(switch3, host8)
    net.addLink(switch3, host9)
    
    net.addLink(switch4, host10)
    net.addLink(switch4, host11)
    net.addLink(switch4, host12)
    




    # Starting network
    net.start()
    
    # Starting Switch output
    s1output=quietRun("ovs-vsctl - - set Bridge s1 ipfix=@i -- --id=@i create IPFIX targets=\"192.168.2.249:2055\" obs_domain_id=123 obs_point_id=456")
    s2output=quietRun("ovs-vsctl - - set Bridge s2 ipfix=@i -- --id=@i create IPFIX targets=\"192.168.2.249:2055\" obs_domain_id=124 obs_point_id=457")
    s3output=quietRun("ovs-vsctl - - set Bridge s3 ipfix=@i -- --id=@i create IPFIX targets=\"192.168.2.249:2055\" obs_domain_id=125 obs_point_id=458")
    s4output=quietRun("ovs-vsctl - - set Bridge s4 ipfix=@i -- --id=@i create IPFIX targets=\"192.168.2.249:2055\" obs_domain_id=126 obs_point_id=459")
    
    print(f"Switch 1:{s1output}\n")
    print(f"Switch 2:{s2output}\n")
    print(f"Switch 3:{s3output}\n")
    print(f"Switch 4:{s4output}\n")

    
    # Ping all
    net.pingAll()

    # iperf
    net.iperf()

    # Enter ClI
    CLI(net)

    # Stopping Network
    time.sleep(duration)
    net.stop()


def information():
    print('H1-1 -> H4-1: ')
    results1 = net.iperf((host1, host10))
    print(results1)
    print('H1-2 -> H3-1: ')
    results2 = net.iperf((host2, host7))
    print(results2)
    print('H2-2 -> H3-2: ')
    results3 = net.iperf((host5, host8))
    print(results3)
    print('H4-3 -> H2-1: ')
    results4 = net.iperf((host12, host4))
    print(results4)
    print('H4-2 -> H1-3: ')
    results5 = net.iperf((host11, host3))
    print(results5)


# Main Function
setLogLevel( 'info' )
emptynet(duration=10)
information()

