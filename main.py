import time
from src import outlook, steam
from constants import driver

original = driver.current_window_handle
driver.implicitly_wait(120)

accname = outlook.create()
print("current account is", accname)
print("Creating steam account...")
driver.switch_to.new_window("tab")
steamwindow = driver.current_window_handle
steam.create(accname)
print("Checking for new mail...")
driver.switch_to.window(original)
outlook.verifysteam()
driver.switch_to.window(steamwindow)
steam.completesignup(accname)
# you can put games you would like the script to claim here, the following is an example
steam.claim(730)
steam.farm(accname)
print("Completed")
