# Nmap Advanced Port Scans

Resources
Read or watch:

    Nmap documentation
    Nmap Advanced Scan
    Everything You Need to Know About Port Scanning
    Advanced Port Scanning techniques
    What is a Port Scanner and How Does it Work?
    How to use Nmap to Scan for Open Ports?
    Nmap to scan all ports
    How to Use Nmap to Scan for Open Ports
    How To Scan All Ports With NMap
    Nmap: TCP and UDP port mapping

References:

    Port Scanning

Learning Objectives


    How to Use Nmap for Advanced Port Scans?
    What are the Different Types of Advanced Port Scans?
    How Advanced Nmap Scans Work?
    What can be detected with Advanced Port Scans?
    What are the use cases and scenarios for Advanced Port Scans?
    What is the main difference between a standard Nmap scan and an advanced port scan?
    What are the differences between a TCP Connect Scan and a SYN Scan ?
    How does an ACK Scan help in determining firewall rules?
    What are FIN, NULL, and Xmas scans, and how can they be used to determine the status of ports on a target system?
    Why do You need Nmap For Securing System Ports?
    What types of information can an advanced port scan reveal about a network?




# Solve the task.

Task #0

0. NULL scan: Hear secrets by pretending not to listen!

Null scans send empty TCP packets to a target. Open ports might silently accept them, while closed ports may respond, giving attackers a clue. They're stealthy.

Write a bash script that executes a TCP NULL scan on a host, targeting ports 20 to 25.

    Your script should accept host as an arguments $1.


Task #1
A FIN scan is a network reconnaissance technique used to identify open ports on a target machine. It works by sending a TCP packet with only the FIN flag set, which typically signifies the end of a connection. By analyzing the target's response, attackers can determine if a port is open, closed, or filtered by a firewall.

FIN scans are attractive because they can sometimes bypass basic firewalls and offer a stealthier approach compared to traditional methods.

Write a bash script that executes a FIN scan on a test network.The scan should identify potential stealth ports, focusing on ports 80 to 85.

    Your script should accept host as an arguments $1.
    Your script should use packet fragmentation to evade packet filters.
    Your script should Adjust the timing option to 2 to reduce scan detectability.

Task #2

2. Xmas scans: turning network packets into holiday lights!

An Xmas scan utilizes TCP packets flagged with FIN, PSH, and URG to stealthily detect open ports, leveraging its unique packet configuration to potentially bypass firewall detection.

This technique, named for its illuminated packet headers, primarily receives responses from closed ports, making it a subtle tool for network analysis.

Write a bash script that executes a xmas scan on a test network.The scan should identify potential stealth ports, focusing on ports 440 to 450.

    Your script should accept host as an arguments $1.
    Your script should only show open (or possibly open) ports.
    Your script should show all packets sent and received.
    Your script should display the reason each port is set to a specific state.


Task #3

3. Maimon scans: the silent knock of network probing!

Maimon scans: like knocking on doors with a magic wand — some ignore you, some slam the door, but you walk away without a trace!

A Maimon scan sends TCP packets with both FIN and ACK flags set to determine port status on a target machine.

Write a bash script that executes a Maimon scan on a test network.The scan should identify potential stealth ports, focusing on scanning the following service ports: http, https, ftp, ssh, and telnet.

    Your script should accept host as an arguments $1.
    Your script should scan ports with high verbosity.

Task #4
The TCP ACK scan is a network probing technique used primarily to determine the filtering rules of a firewall. By sending a packet with the ACK flag set to various ports, and observing whether the target responds with an RST packet, security professionals can infer whether ports are statefully inspected.

You are a network administrator responsible for verifying the firewall rules for a newly deployed section of your corporate network. Before deploying critical services, you want to ensure that the firewall is properly filtering unexpected external ACK packets, which should all be blocked or filtered to enhance security against potential reconnaissance activities by attackers.

Write a bash script that performs a TCP ACK scan on a specified test network. The scan should identify potential stealth ports, focusing on ports 80, 22, 25.

    Your script should accept host as an arguments $1.
    Your script should accept ports as an arguments $2.
    Your script should display the reason each port is set to a specific state.
    Your script should enforce a time limit of 1000 milliseconds for each host response.

Task #5

5. TCP Window Scan: Like checking a letter's fine print to see if you're invited!

The TCP Window scan refines the technique used in ACK scans by analyzing the |TCP window size of RST packets returned from a target. If a port is open, the TCP window size in the RST packet is often non-zero, subtly indicating an active listening state, whereas closed ports generally return a zero window size.

This method is useful when more common scans like SYN are blocked, offering an alternative for deducing port status.

Write a bash script that performs a a TCP Window scan on a specified test network. The scan should identify potential stealth ports, in the range from 20 to 30, but exclude ports from 25to 28.

    Your script should accept host as an arguments $1.
    Your script should accept ports as an arguments $2.
    Your script should accept a range of ports to exclude as an argument $3.


Task #6

6. Custom Scan: Because even network security likes its coffee made a certain way!

A Custom Scan is a targeted method used in network security to evaluate specific vulnerabilities or areas within a network. It enables cybersecurity experts to focus on particular segments, ports, or protocols, optimizing resources and identifying critical weaknesses more effectively.

The security team decides to use an advanced Nmap scan that manipulates TCP flags to create non-standard packets, which are typically not used in regular communications but might be utilized by attackers to probe and exploit vulnerabilities in network defenses.

Write a bash script that executes a custom scan. The script should configure Nmap to send packets with all possible TCP flags set, targeting ports 80 to 90 on a specified host.

    Your script should accept host as an arguments $1.
    Your script should accept ports as an arguments $2.
    Your script should save the output to the file custom_scan.txt.
    Your script should redirect both error messages and standard output to ensure nothing appears on the screen.


