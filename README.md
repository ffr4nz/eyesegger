# EyesEgger

Simple API REST to scan port over an IPv6 address usinf python socket lib

> A port scan or portscan can be defined as a process that sends client requests to a range of server port addresses on a host, with the goal of finding an active port. While not a nefarious process in and of itself, it is one used by hackers to probe target machine services with the aim of exploiting a known vulnerability of that service,[1] however the majority of uses of a port scan are not attacks and are simple probes to determine services available on a remote machine.

## Description

EyesEgger is just a micro service covering IPv6 port scan functionality over an API/JSON interface.

### Installation

Get last version from Github repo:

```sh
$ git clone https://github.com/ffr4nz/eyesegger.git
```

You need some requeriment installed:

```sh
$ pip install -r requirements.txt
```

After pip install all libraries service can start using:

```sh
$ python sixcansrv.py -p 4343
```
Consume API service using */ip/* endpoint

**http://eyesegger.server.domain:service-port/ip/IPv6-ADDR/PORT/PROTOCOL**

**http://eyesegger.server.domain:service-port/ip/2001:1838:2007:0::1/22/tcp**
```json

{
"dest_ip": "2001:1838:2007:0::1",
"epoch_date": 1441367312000",
"port": "22","response": "SSH-2.0-OpenSSH_6.0\r\n",
"status": "success",
"str_date": "04-09-15_07:48"
}

```

License
----

GPL

References
----

