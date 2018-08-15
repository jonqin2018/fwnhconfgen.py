#!/usr/bin/python
import jinja2
import re
import datetime
import os
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

# Create the jinja2 environment.
# Notice the use of trim_blocks greatly helps control whitespace.
j2_env = Environment(loader=FileSystemLoader(template_dir),trim_blocks=True)
template = j2_env.get_template('fwsm_nh_acl_template')

def removews(my_string):
    """remove extra white string"""
    return ([x.strip() for x in my_string.split(',')])

rvar = dict()

rvar["netobjnames"] = [         
                {
                'name': '',
                'objdescr':'',
                'network':'',
                'nwkdescr':'', 
                }
                        ]
                        
rvar["portobjnames"] = [         
                {
                'name': '',
                'objdescr':'',
                'portdescr':'',
                'protocol':'', 
                'port':'',
                'udp':'',
                }
                        ]

tempvar = dict()

#### raw_inputs

isthisnewnetobj = raw_input("create new network objects? y or any other key-->  ")

if isthisnewnetobj == 'y':
    # new L1 network object
    netobjname    = removews(raw_input("object name? --> "))
    rvar["newnetobj"]  = True
    count = len(netobjname)
    for i in range(0,count):
        print ("\n" + str(count) + " network objects will be created")
        print ("\nraw_input info for " + netobjname[i] ) 
        tempvar['name'] = netobjname[i]
        tempvar['objdescr']   = raw_input("description -->  ")
        tempvar['network']    = removews(raw_input("network --> "))
        tempvar['nwkdescr']   = raw_input("network description -->  ")
        rvar["netobjnames"].append(tempvar)       
        print

tempvar = {}

isthisnewportobj = raw_input("\ncreate new tcp port object? y or Enter -->  ")

if isthisnewportobj == 'y':
    # new L1 port object
    portobjname   = removews(raw_input("name: "))
    rvar["newportobj"] = True
    count = len(portobjname)
    for i in range(0,count):
        print (str(count) + " tcp objects will be created")
        print ("raw_input info for " + portobjname[i] )       
        tempvar['name'] =   portobjname[i]  
        tempvar['objdescr']  = raw_input("description:  ")
        tempvar['protocol']  = 'tcp'
        tempvar['port']      = removews(raw_input("tcp ports (eq 135): "))
        tempvar['portdescr'] = raw_input("port description: ")
        rvar["portobjnames"].append(tempvar)  
        
tempvar ={}
isthisnewportobj = raw_input("\ncreate new udp object? y or Enter -->  ")

if isthisnewportobj == 'y':
    # new L1 port object
    portobjname   = removews(raw_input("name: "))
    rvar["newportobj"] = True
    count = len(portobjname)
    for i in range(0,count):
        print (str(count) + " udp objects will be created")
        print ("raw_input info for " + portobjname[i] )       
        tempvar['name'] =   portobjname[i]  
        tempvar['objdescr']  = raw_input("description:  ")
        tempvar['protocol']  = 'udp'
        tempvar['port']      = removews(raw_input("tcp ports (eq 53): "))
        tempvar['portdescr'] = raw_input("port description: ")
        rvar["portobjnames"].append(tempvar)  
        

print  ("\n")

# l2 rule"
rulenumber    = raw_input("rule number (eg. 10):   ")
rulerange     = raw_input("rule range (eg. ten31): ")
securityid    = raw_input("security id (lhrissercom):  ")
ruledescr     = raw_input("rule description:  ")
srcobj        = removews(raw_input("source object group or network:"))
dstobj        = removews(raw_input("destination object group or network:"))
tcp           = removews(raw_input("tcp ports: "))
udp           = removews(raw_input("udp ports: "))
enableicmp    = raw_input("enable icmp? ")
enablelayer3  = raw_input("enable layer3? ")

       
rvar["sssiiicccaaa"] = securityid
rvar["iprange"] = rulerange
rvar["customnumber"] = ' custom-' + rulenumber
rvar["cnumber"] = 'c' + rulenumber
rvar["insttime"] = datetime.date.today().strftime('%y%m%d')
rvar["ruledescr"] = ruledescr 
rvar["srcobj"] = srcobj 
rvar["dstobj"] = dstobj
rvar["enableicmp"] = enableicmp
rvar["enablelayer3"] = enablelayer3
rvar["tcp"] = tcp
rvar["udp"] = udp


print (template.render(rvar))
