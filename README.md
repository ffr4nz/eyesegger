# WhoAreYou

Simple API REST to get Whois data using Python-Whois

> WHOIS (pronounced as the phrase who is) is a query and response protocol that is widely used for querying databases that store the registered users or assignees of an Internet resource, such as a domain name, an IP address block, or an autonomous system, but is also used for a wider range of other information. The protocol stores and delivers database content in a human-readable format.

## Description

WhoAreYou is just a micro service covering Whois services on Unix-like system with an API/JSON interface.

### Installation

Get last version from Github repo:

```sh
$ git clone https://github.com/ffr4nz/whoareyou.git
```

You need some requeriment installed:

```sh
$ pip install -r requirements.txt
```

After pip install all libraries service can start using:

```sh
$ python whoiservice.py -p 4343
```
Consume API service using */whois/* endpoint

**http://whoareyou.server.domain:4343/whois/google.com**

```json
{
    "contacts": 
{
    "admin": 
{
    "city": "Mountain View",
    "country": "US",
    "email": "dns-admin@google.com",
    "fax": "+1.6506188571",
    "name": "DNS Admin",
    "organization": "Google Inc.",
    "phone": "+1.6506234000",
    "postalcode": "94043",
    "state": "CA",
    "street": "1600 Amphitheatre Parkway"
},
"billing": null,
"registrant": 
{
    "city": "Mountain View",
    "country": "US",
    "email": "dns-admin@google.com",
    "fax": "+1.6506188571",
    "name": "Dns Admin",
    "organization": "Google Inc.",
    "phone": "+1.6502530000",
    "postalcode": "94043",
    "state": "CA",
    "street": "Please contact contact-admin@google.com, 1600 Amphitheatre Parkway"
},
"tech": 
    {
        "city": "Mountain View",
        "country": "US",
        "email": "dns-admin@google.com",
        "fax": "+1.6506181499",
        "name": "DNS Admin",
        "organization": "Google Inc.",
        "phone": "+1.6503300100",
        "postalcode": "94043",
        "state": "CA",
        "street": "2400 E. Bayshore Pkwy"
    }

},
"creation_date": 
[
    "Mon, 15 Sep 1997 00:00:00 GMT"
],
"emails": 
[
    "abusecomplaints@markmonitor.com",
    "contact-admin@google.com"
],
"expiration_date": 
[
    "Sun, 13 Sep 2020 21:00:00 GMT",
    "Sun, 13 Sep 2020 21:00:00 GMT"
],
"id": 
[
    "2138514_DOMAIN_COM-VRSN"
],
"nameservers": 
[
    "ns4.google.com",
    "ns2.google.com",
    "ns3.google.com",
    "ns1.google.com"
],
"raw": 
[
    "Domain Name: google.com\nRegistry Domain ID: 2138514_DOMAIN_COM-VRSN\nRegistrar WHOIS Server: whois.markmonitor.com\nRegistrar URL: http://www.markmonitor.com\nUpdated Date: 2015-06-12T10:38:52-0700\nCreation Date: 1997-09-15T00:00:00-0700\nRegistrar Registration Expiration Date: 2020-09-13T21:00:00-0700\nRegistrar: MarkMonitor, Inc.\nRegistrar IANA ID: 292\nRegistrar Abuse Contact Email: abusecomplaints@markmonitor.com\nRegistrar Abuse Contact Phone: +1.2083895740\nDomain Status: clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)\nDomain Status: clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)\nDomain Status: clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)\nRegistry Registrant ID: \nRegistrant Name: Dns Admin\nRegistrant Organization: Google Inc.\nRegistrant Street: Please contact contact-admin@google.com, 1600 Amphitheatre Parkway\nRegistrant City: Mountain View\nRegistrant State/Province: CA\nRegistrant Postal Code: 94043\nRegistrant Country: US\nRegistrant Phone: +1.6502530000\nRegistrant Phone Ext: \nRegistrant Fax: +1.6506188571\nRegistrant Fax Ext: \nRegistrant Email: dns-admin@google.com\nRegistry Admin ID: \nAdmin Name: DNS Admin\nAdmin Organization: Google Inc.\nAdmin Street: 1600 Amphitheatre Parkway\nAdmin City: Mountain View\nAdmin State/Province: CA\nAdmin Postal Code: 94043\nAdmin Country: US\nAdmin Phone: +1.6506234000\nAdmin Phone Ext: \nAdmin Fax: +1.6506188571\nAdmin Fax Ext: \nAdmin Email: dns-admin@google.com\nRegistry Tech ID: \nTech Name: DNS Admin\nTech Organization: Google Inc.\nTech Street: 2400 E. Bayshore Pkwy\nTech City: Mountain View\nTech State/Province: CA\nTech Postal Code: 94043\nTech Country: US\nTech Phone: +1.6503300100\nTech Phone Ext: \nTech Fax: +1.6506181499\nTech Fax Ext: \nTech Email: dns-admin@google.com\nName Server: ns4.google.com\nName Server: ns2.google.com\nName Server: ns3.google.com\nName Server: ns1.google.com\nDNSSEC: unsigned\nURL of the ICANN WHOIS Data Problem Reporting System: http://wdprs.internic.net/\n>>> Last update of WHOIS database: 2015-07-23T03:15:44-0700 <<<\n\nThe Data in MarkMonitor.com's WHOIS database is provided by MarkMonitor.com for\ninformation purposes, and to assist persons in obtaining information about or\nrelated to a domain name registration record.  MarkMonitor.com does not guarantee\nits accuracy.  By submitting a WHOIS query, you agree that you will use this Data\nonly for lawful purposes and that, under no circumstances will you use this Data to:\n (1) allow, enable, or otherwise support the transmission of mass unsolicited,\n     commercial advertising or solicitations via e-mail (spam); or\n (2) enable high volume, automated, electronic processes that apply to\n     MarkMonitor.com (or its systems).\nMarkMonitor.com reserves the right to modify these terms at any time.\nBy submitting this query, you agree to abide by this policy.\n\nMarkMonitor is the Global Leader in Online Brand Protection.\n\nMarkMonitor Domain Management(TM)\nMarkMonitor Brand Protection(TM)\nMarkMonitor AntiPiracy(TM)\nMarkMonitor AntiFraud(TM)\nProfessional and Managed Services\n\nVisit MarkMonitor at http://www.markmonitor.com\nContact us at +1.8007459229\nIn Europe, at +44.02032062220\n--\n",
    "   Domain Name: GOOGLE.COM\n   Registrar: MARKMONITOR INC.\n   Sponsoring Registrar IANA ID: 292\n   Whois Server: whois.markmonitor.com\n   Referral URL: http://www.markmonitor.com\n   Name Server: NS1.GOOGLE.COM\n   Name Server: NS2.GOOGLE.COM\n   Name Server: NS3.GOOGLE.COM\n   Name Server: NS4.GOOGLE.COM\n   Status: clientDeleteProhibited http://www.icann.org/epp#clientDeleteProhibited\n   Status: clientTransferProhibited http://www.icann.org/epp#clientTransferProhibited\n   Status: clientUpdateProhibited http://www.icann.org/epp#clientUpdateProhibited\n   Status: serverDeleteProhibited http://www.icann.org/epp#serverDeleteProhibited\n   Status: serverTransferProhibited http://www.icann.org/epp#serverTransferProhibited\n   Status: serverUpdateProhibited http://www.icann.org/epp#serverUpdateProhibited\n   Updated Date: 20-jul-2011\n   Creation Date: 15-sep-1997\n   Expiration Date: 14-sep-2020"
],
"registrar": 
[
    "MarkMonitor, Inc."
],
"status": 
[
    "clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)",
    "clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)",
    "clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)"
],
"updated_date": 
[
    "Fri, 12 Jun 2015 10:38:52 GMT"
],
"whois_server": 
    [
        "whois.markmonitor.com"
    ]
}
```

License
----

GPL

References
----

[1] The WHOIS protocol is documented in RFC 3912
