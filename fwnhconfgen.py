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

#### inputs

isthisnewnetobj = input("create new network objects? y or any other key-->  ")

if isthisnewnetobj == 'y':
    # new L1 network object
    netobjname    = removews(input("object name? --> "))
    rvar["newnetobj"]  = True
    count = len(netobjname)
    for i in range(0,count):
        print ("\n" + str(count) + " network objects will be created")
        print ("\ninput info for " + netobjname[i] ) 
        tempvar['name'] = netobjname[i]
        tempvar['objdescr']   = input("description -->  ")
        tempvar['network']    = removews(input("network --> "))
        tempvar['nwkdescr']   = input("network description -->  ")
        rvar["netobjnames"].append(tempvar)       
        print

tempvar = {}

isthisnewportobj = input("\ncreate new tcp port object? y or Enter -->  ")

if isthisnewportobj == 'y':
    # new L1 port object
    portobjname   = removews(input("name: "))
    rvar["newportobj"] = True
    count = len(portobjname)
    for i in range(0,count):
        print (str(count) + " tcp objects will be created")
        print ("input info for " + portobjname[i] )       
        tempvar['name'] =   portobjname[i]  
        tempvar['objdescr']  = input("description:  ")
        tempvar['protocol']  = 'tcp'
        tempvar['port']      = removews(input("tcp ports (eq 135): "))
        tempvar['portdescr'] = input("port description: ")
        rvar["portobjnames"].append(tempvar)  
        
tempvar ={}
isthisnewportobj = input("\ncreate new udp object? y or Enter -->  ")

if isthisnewportobj == 'y':
    # new L1 port object
    portobjname   = removews(input("name: "))
    rvar["newportobj"] = True
    count = len(portobjname)
    for i in range(0,count):
        print (str(count) + " udp objects will be created")
        print ("input info for " + portobjname[i] )       
        tempvar['name'] =   portobjname[i]  
        tempvar['objdescr']  = input("description:  ")
        tempvar['protocol']  = 'udp'
        tempvar['port']      = removews(input("tcp ports (eq 53): "))
        tempvar['portdescr'] = input("port description: ")
        rvar["portobjnames"].append(tempvar)  
        

print  ("\n")

# l2 rule"
rulenumber    = input("rule number (eg. 10):   ")
rulerange     = input("rule range (eg. ten31): ")
securityid    = input("security id (lhrissercom):  ")
ruledescr     = input("rule description:  ")
srcobj        = removews(input("source object group or network:"))
dstobj        = removews(input("destination object group or network:"))
tcp           = removews(input("tcp ports: "))
udp           = removews(input("udp ports: "))
enableicmp    = input("enable icmp? ")
enablelayer3  = input("enable layer3? ")

       
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
