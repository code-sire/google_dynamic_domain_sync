# -*- coding: utf-8 -*-


#  Import whatever is needed
import os
import logging
import requests
import re
import datetime

from sys import exit 


# User Variables
conf_username = ''
conf_password = ''

# domainurl = '@.example.com'
domainurl = '' 



# Global Variables

gv_logpath = "/usr/local/bin/log"
gv_logfile = 'gddu.log'

gv_UpdateUrl = 'https://${user}:${pass}@domains.google.com/nic/update?hostname=${domain}&myip=${ip}'
gv_external_ip ='https://domains.google.com/checkip'



# Function used to log.
def Logging(def_msg):

    # Making sure the logging folder is present. If not it will be created.
    if os.path.exists(gv_logpath):
        pass
    else:
        os.makedirs(gv_logpath)

    # Setting the full log path.
    full_log_path = gv_logpath + "/" + gv_logfile

    # Pulling time at the moment.
    current_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")

    # Logging to the Console
    print (def_msg)
    print(current_time)
    print('')

    # Logging to File
    with open(full_log_path, "a") as logfile:
        logfile.write('----------------------------------------------------------\n')
        logfile.write(str(current_time) + " " + str(def_msg) + "\n")


# Pulling the External IP
def PullIP():
    ipresponse = requests.get(gv_external_ip, timeout=5)
    ip = ipresponse.text
    return ip


# Building the string for the API
def buildupdateurl():
    ip = PullIP()
    
    global gv_UpdateUrl
    
    gv_UpdateUrl = gv_UpdateUrl.replace('${user}', conf_username)
    gv_UpdateUrl = gv_UpdateUrl.replace('${pass}', conf_password)
    gv_UpdateUrl = gv_UpdateUrl.replace('${domain}', domainurl)
    gv_UpdateUrl = gv_UpdateUrl.replace('${ip}', ip)

    
 
    
# Starting things 
buildupdateurl()    
submit_response = requests.get(gv_UpdateUrl, timeout=5)
Logging("Response: " + submit_response.text)

