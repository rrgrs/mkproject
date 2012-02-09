#!/usr/bin/env python

import sys, os, base64

import data

if (len(sys.argv) < 1):
	sys.exit('project name parameter required')
	
INIT_FILE = '__init__.py'
	
def mkdir(path):
    if os.path.exists(path) == False:
        os.makedirs(path)
    return True
    
def mkinit(path):
    p = os.path.join(path, INIT_FILE)
    open(p, 'w')
    return True
    
def wtinit(path, data):
    init = open(os.path.join(path, INIT_FILE), 'w')
    init.write(data)
    init.close()
	
p_name = sys.argv[1]


mkdir(p_name)
	
open(os.path.join(p_name, INIT_FILE), 'w').close()

	
inner_dirs = [
    {'name': 'apps', 'create_init': True},
    {'name': 'deps', 'create_init': True},
    {'name': 'static', 'create_init': False},
    {'name': 'media', 'create_init': False},
    {'name': 'apache', 'create_init': False},
    {'name': 'fixtures', 'create_init': False},
    {'name': 'templates', 'create_init': False},
    {'name': p_name, 'create_init': True},
]
#make inner dirs
for i_dir in inner_dirs:
    p = os.path.join(p_name, i_dir['name'])
    mkdir(p)
    if i_dir['create_init']:
        mkinit(p)
        

p_dirs = [
    'settings',
    'urls',
]
#make settings and url dirs
for d in p_dirs:
    p = os.path.join(p_name, p_name, d)
    mkdir(p)
    mkinit(p)
    
s_dirs = [
    {'name': 'production', 'data': data.settings['production'] % {'p_name': p_name}},
    {'name': 'staging', 'data': data.settings['staging'] % {'p_name': p_name}},
]
#write settings init files and populate with data
for s_dir in s_dirs:
    p = os.path.join(p_name, p_name, 'settings', s_dir['name'])
    mkdir(p)
    mkinit(p)
    wtinit(p, s_dir['data'])


#insert initial settings data
key = base64.urlsafe_b64encode(os.urandom(37))[:-2]
wtinit(os.path.join(p_name, p_name, 'settings'), data.settings['reg'] % {'p_name': p_name, 'key': key})
#write urls file
wtinit(os.path.join(p_name, p_name, 'urls'), data.urls)

#create and populate manage.py file
f = open(os.path.join(p_name, p_name, 'manage.py'), 'w')
f.write(data.manage)
f.close()

#write apache files
f = open(os.path.join(p_name, 'apache', 'production'), 'w')
f.write(data.apache['production'])
f.close()
f = open(os.path.join(p_name, 'apache', 'staging'), 'w')
f.write(data.apache['staging'])
f.close()
    