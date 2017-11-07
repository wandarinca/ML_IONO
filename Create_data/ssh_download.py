#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:25:58 2017
ssh download something
@author: wanda
"""
from os import listdir, sep, mkdir, system
#home/wanda/plots_events_2014_regme
year = "2014"
days2download = listdir("/home/wanda/plots_events_2014_regme"+sep+year)
print days2download
#Download Gradients folder for every day 
#/mnt/gnss/data/rap/Andaluza/module_results_regme/processed_nobias/YYYY/DDD/Gradients
#sshpass -p password scp -o User=username -o StrictHostKeyChecking=no src dst:/path
#sshpass -p "password" scp -r user@example.com:/some/remote/path /some/local/path

host = '####'
user = '####'
pw = '####'
red = 'regme'

output_folder = "/home/wanda/Iono_Classifier/"+red
# SCPCLient takes a paramiko transport as its only argument
def scp_folder_remote2local(year, doy, host, user, pw, folder_remote):
    # Make sure the directory exists or create it 
    if year not in listdir(output_folder):
        try:
            mkdir(output_folder+sep+year)

        except OSError, e:
            if e.errno != 17:
                raise
                pass
    if doy not in listdir(output_folder+sep+year):
        try:
            mkdir(output_folder+sep+year+sep+doy)

        except OSError, e:
            if e.errno != 17:
                raise  
                pass
    folder_local = output_folder+sep+year+sep+doy
    command = "sshpass -p "+pw+" scp -r "+user+"@"+host+":"+folder_remote+" "+folder_local
    print command
    system(command)

for doy in days2download:
    folder_remote = "/mnt/gnss/data/rap/Andaluza/module_results_regme/processed_nobias/"+year+"/"+doy+"/Gradients"
    scp_folder_remote2local(year, doy, host, user,pw, folder_remote)
    
    
