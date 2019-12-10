# IOT (Internet Of Things)
Wireless IOT 

Scapy Version 2.4.3 is use to extract features form the wireless traffic payload.For more detail please visit https://github.com/secdev/scapy
The code is tested on Python 3.6.8 at the time of creation. 
Airodump-ng 1.2 rc4 is used to collect the wireless traffic in monitoring mode with help of airmon-ng. For more detail please visit http://www.aircrack-ng.org

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
The code is wirtten in one of its simplest and efficent way with help of python based scapy program. Scapy features in-built functions which is handy and 
helpful to analyze the network communication packets. 

SETUP

Aircrack-ng package must be installed on the system before we start to collect (sniff) wrieless packet. A monitoring mode enabled wireless network adaptor must be instlled 
on sniffing device. 

OPERTING SYSTEM (OS)

Ubuntu 18.04.2 LTS Linux 4.15.0-72-generic 

HANDY COMMANDS

List Wireless enabled interface
$ iwconfig 

Enable monitoring mode on wireless network adaptor (Must be root user to execute the following command)
#airmon-ng start <interfacename>

Sniff/Dump Wireless packets 
#airodump-ng <monitoring_interfacename>
We can sniff the specific wireless access point wireless communication packets. After we enabled wirelss monitoring mode on the wireless adaptor. 
we can run "iwlist <monitoring_interfacename> scanning" commond to scan the wireless network available within a range. 

Once the wireless monitoring mode is setup we can write a simple python program to sniff the wireless packets with help of scapy. 
Please find a sample code sniff.py. 

A sample pcap file is available with in the IOT repository folder. Run the IOT_Wirless.py to extract wireless packets payload save in a csv labeled file.
Which can be further use in machine learning tool like weka for analysis.

NOTE: If the csv file didn't load on weka.Please save the file again and try. 



