# DNS Resolver

## About
Simple DNS resolver with cache

## Requirements

Python >=3.8.
dnspython==2.2.1


## Usage
First start DNS server from project root

```bash
sudo python -m resolver

;; Started DNS server on localhost:53
```
## Examples

```bash
dig google.com @127.0.0.1

; <<>> DiG 9.18.1-1ubuntu1.2-Ubuntu <<>> google.com @127.0.0.1
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 47309
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: e8e0595ca6a3222a (echoed)
;; QUESTION SECTION:
;google.com.                    IN      A

;; ANSWER SECTION:
google.com.             300     IN      A       216.58.215.46

;; Query time: 76 msec
;; SERVER: 127.0.0.1#53(127.0.0.1) (UDP)
;; WHEN: Wed Nov 02 11:27:38 CET 2022
;; MSG SIZE  rcvd: 67

