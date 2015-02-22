#!/user/bin/env python
"""
1)
Resolve the DNS/IP address of a given domain

  1.1 use nmap dns-brute
    nmap --script dns-brute -sn <ip/domain>
  1.2 use netcraft
    http://toolbar.netcraft.com/site_report?url=<ip/domain>
  1.3 use resloveip
    resloveip <ip/domain>
2)
Use CloudFlare Watch
  http://www.crimeflare.com/cfs.html

"""
import socket

def getIP(d):
    try:
        data = socket.gethostbyname(d)
        ip = repr(data)
        return ip
    except Exception:
        return False

def getIPx(d):
    try:
        data = socket.gethostbyname_ex(d)
        ipx = repr(data[2])
        return ipx
    except Exception:
        return False

def getHost(ip):
    try:
        data = socket.gethostbyaddr(ip)
        host = repr(data[0])
        return host
    except Exception:
        return False

def getAlias(d):
    try:
        data = socket.gethostbyname_ex(d)
        alias = repr(data[1])
        return alias
    except Exception:
        return False



domain = raw_input("Domain name > ")

subdomain = [
              '', 'www', 'm', 'ssl',
              'blog', 'board', 'forum',
              'test', 'dev', 'beta',
              'webmail', 'mail', 'email',
              'support', 'help',
              'direct', 'direct-connect', 'direct-connect-mail',
              'ftp', 'imap', 'smtp',
              'record', 'dns', 'ns', 'ns1', 'ns2', 'ns3', 'ns4',
              'irc', 'server', 'status', 'portal',
              'cpanel',
            ]

for sub in subdomain:
  if(sub):
    target = sub + '.' + domain
  else:
    target = domain

  print target
  IP = getIP(target)
  IPx = getIPx(target)
  HOST = getHost(target)
  ALIAS = getAlias(target)

  if(IP): print "\tIP ", IP
  if(IPx): print "\tIPx ", IPx
  if(HOST): print "\tHost ", HOST
  if(ALIAS): print "\tAlias ", ALIAS
