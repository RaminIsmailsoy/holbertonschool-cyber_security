# Passive Reconnaissance

Resources
Read or watch:
What is passive reconnaissance ?
WHOIS
What is DNS?
What is a DNS server?
How to Install and Use Subfinder?
References
Unified Kill Chain
RFC-3912
whois
dig
dnslookup
shodan.io
DNSDumpster
Google Hacking


Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

What can we learn about a Server
What is a DNS server
What happens when we type www.holbertonschool.com and press ENTER
How can we find the owner information for a domain name
What is dig
What is nslookup
What are the different types of DNS RECORDS
What is DNS Dumpster
What is Shodan.io
How can we find subdomains
What is subfinder
What is the difference between Active reconnaissance and Passive reconnaissance


Tasks
0. Who is it ?
mandatory
Write a bash script that extract using whois scan in csv format:

Registrant Information
Admin Information
Tech Information
hints:

You are only allowed to use awk to format your output

Use awk print “Field,Value” to format each line.

Add space after Street fields (e.g., “Street,5670 Wilshire Blvd ”).

Include colon in Ext fields even if empty: “Phone Ext:,”.

Ensure no extra newline at the end of the file.



