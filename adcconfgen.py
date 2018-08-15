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
template = j2_env.get_template('adc_basic_ssl_template')

#### inputs
vipname = raw_input("vip name (example A200)  :  ")
vipdomainname = raw_input("domain name   : ")
vipprobeurl   = raw_input("probe url   : ")
rservername   = raw_input("rserver name (eg. vweb1611,vweb1612)   :").split(",")
rserverip     = raw_input("rserver ip (eg. 10.44.140.11,10.44.140.12)   :").split(",")
serviceport   = raw_input("server service port (eg. 8080)  :  ")

vipservicename = '-'.join((vipname,vipdomainname)).upper()
vipservicename = vipservicename.replace('.', '-')

if 'IS-SAIT-CA'  == vipservicename[-10:]:
    vipsslcert = 'STAR_IS_SAIT_CA'
elif '-SAIT-CA' == vipservicename[-8:]:
    vipsslcert = 'STAR-SAIT-CA_REV2'
else:
    print ("Wrong cert")
    exit()

# build server, ip and port list
sgitem = {}
sgservers = []

for i in range(len(rservername)):
    sgitem['name'] = rservername[i] 
    sgitem['ip']   = rserverip[i]
    sgitem['port'] = str(serviceport)  
    sgservers.append(sgitem.copy())

#sgservers = [
#    {
#        'name': 'vtest001',
#        'ip': '172.16.0.1',
#        'port': '8080'
#    },
#    {
#        'name': 'vtest002',
#        'ip': '172.16.0.2',
#        'port': '8080'
#    },
#]


rvar = dict()

#Todo: add selector based on inputs

# start parsing out inputs and populating template vars
if vipprobeurl == '':
    vipprobeurl = '/'

vmatch = re.match('^([A,B,C,D])(\d{1,3})-.*', vipservicename)
vipnum = vmatch.group(2)
if vmatch.group(1) == 'A':
    rvar["vipips"] = [
        {
            'desc': '#@I cisco3743 tt209',
            'ip': '10.12.32.' + vipnum
        },
        {
            'desc': '#@J cisco3745 md005',
            'ip': '10.12.96.' + vipnum
        },
    ]
elif vmatch.group(1) == 'B':
    rvar["vipips"] = [
        {
            'desc': '#@I cisco3743 tt209',
            'ip': '10.12.33.' + vipnum
        },
        {
            'desc': '#@J cisco3745 md005',
            'ip': '10.12.97.' + vipnum
        },
    ]
elif vmatch.group(1) == 'C':
    rvar["vipips"] = [
        {
            'desc': '#@I cisco3743 tt209',
            'ip': '10.12.34.' + vipnum
        },
        {
            'desc': '#@J cisco3745 md005',
            'ip': '10.12.98.' + vipnum
        },
    ]

elif vmatch.group(1) == 'D':
    rvar["vipips"] = [
        {
            'desc': '#@I cisco3743 tt209',
            'ip': '10.12.35.' + vipnum
        },
        {
            'desc': '#@J cisco3745 md005',
            'ip': '10.12.99.' + vipnum
        },
    ]

else:
    print ("Error:  Couldn't parse VIP ID")
    sys.exit(1)


rvar["vipprobeurl"] = vipprobeurl
rvar["vipservicename"] = vipservicename
rvar["vipid"] = vmatch.group(1)+vmatch.group(2)
rvar["vipnum"] = vipnum
rvar["vipdomainname"] = vipdomainname
rvar["vipsslcert"] = vipsslcert
rvar["edited"] = 'cq' + datetime.date.today().strftime('%y%m%d')
rvar["sgservers"] = sgservers

# render the doc
print (template.render(rvar))


