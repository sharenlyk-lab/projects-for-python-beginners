import os  #toolbox to control files and system 
from time import sleep #pause progam 
import pickle #save and load python projects 
from selenium import webdriver 

#“load Selenium’s browser‑control tool so Python can open and automate a web browser
#now we are opening microsoft edge 

from selenium.webdriver.common.by import By

#Open Microsoft Edge 

driver= webdriver.Edge()

#CityLink Webpage
citylink_url=("shows.cityline.com.hk/en/2026/treasuretour26.html")

driver.get("https://shows.cityline.com.hk/en/2026/treasuretour26.html")

sleep(30)


    



