from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


password = "somerandompassword123"
asflocation = "asf root folder goes here"

password = "passwordgoeshere123"
asflocation = "ASF LOCATION GOES HERE"

# this is the name for both the steam account and the Outlook email (random numbers will be added to the end of both)
usrname = "somerandomname"
firstname = "somerandomfirstname"
lastname = "somerandomlastname"
