# -*- coding: utf-8 -*-
"""
Created on Mon May 18 13:37:25 2021

This is a TextBot for whatsApps web app

CHANGE file_name, user_name, and geckdriver to what you want

once you open it you will have 5 seconds to scan your whatsapp QR code from your phone in order
to login

@author: Mike Sal
"""

from selenium import webdriver
import time


#this is where you will put the moviescript file
file_name = "rotsScript2.txt"
##############################################################################
#change recipient here
user_name = 'Planning'       
##############################################################################
#change geckodriver file location here
geckodriver = 'C:\\Users\Mike Sal\Desktop\Drivers\geckodriver'
##############################################################################

movieTextFile = open(file_name, "r")
script = movieTextFile.readlines()
movieTextFile.close()

firefox_browser = webdriver.Firefox(executable_path= geckodriver)
firefox_browser.get('https://web.whatsapp.com/')

time.sleep(10)

print('Scanning Complete...')

user = firefox_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()

message_box = firefox_browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
send_button = firefox_browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]')


for line in script:
    message_box.send_keys(line)
    #send_button.click()
    total = 1
    i = 0

    while(i < len(line)):
        if(line[i] == ' '):
            total = total + 1
        i = i + 1
        
    time.sleep(.5)
    
    
