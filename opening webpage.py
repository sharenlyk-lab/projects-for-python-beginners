import os  #toolbox to control files and system 
from time import sleep #pause progam 
import pickle #save and load python projects 
from selenium import webdriver 

#“load Selenium’s browser‑control tool so Python can open and automate a web browser
#now we are opening microsoft edge 

from selenium.webdriver.common.by import By

#Open Microsoft Edge 

driver= webdriver.Edge()

#Google webpage
google_url=("https://www.google.com/")

driver.get("https://www.google.com/")

sleep(30)


    




