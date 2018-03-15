#!/usr/bin/env python

import re
import socket
import sys

writeFileName_='writefile.txt'
readFileName_='readfile.txt'

def pingcheck(hostname):
    try:
        socket.gethostbyname(hostname)
        # print(x)
        return True
    except socket.error:
        return False

def parseEmail( readFileName,writeFileName ):
    writeFile = open(writeFileName,'w')
    readFile = open(readFileName,'r')
    lines_read=readFile.readlines()
    readFile.close()
    
    lines = list(set(lines_read))
    lines.sort()
    EMAIL = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}", re.IGNORECASE)
    HOST = re.compile(r"@[A-Z0-9.-]+\.[A-Z]{2,4}",re.IGNORECASE)
    # USER = re.compile(r"[A-Z0-9._%+-]",re.IGNORECASE)
    domain_ids = dict()
    
    for emails in lines:
        match = re.findall( EMAIL, emails )
        for email in match:
            host = re.findall ( HOST , email )[0].replace('@','')
            try:
                if domain_ids[host]:
                    writeFile.write(email)
            except KeyError:
                x = pingcheck(host)
                domain_ids[host] = x
                if x:
                    writeFile.write(email)
                    print(len(domain_ids))
    writeFile.close()

parseEmail(readFileName_, writeFileName_)
