import time
import json
import keyboard
from constants import password, driver, asflocation
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def create(username):
    email = username + "@outlook.com"
    driver.get("https://store.steampowered.com/join/?redir=%3Fl%3Dfrench&snr=1_60_4__62")
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "reenter_email").send_keys(email)
    country = driver.find_element(By.ID, "country")
    # setting this to a country in the EU might cause issues
    Select(country).select_by_value("EG")
    driver.find_element(By.ID, "i_agree_check").click()
    keyboard.wait('c')
    driver.find_element(By.ID, "createAccountButton").click()


def completesignup(username):
    driver.find_element(By.ID, "accountname").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "reenter_password").send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='createAccountButton']/span").click()
    driver.find_element(By.XPATH, "//*[@id='foryou_tab']/span/a[2]")



def claim(appid):
    driver.get("https://store.steampowered.com/app/" + str(appid))
    driver.find_element(By.XPATH, "//span[contains(text(), 'Add to Library')]").click()
    driver.find_element(By.XPATH, "/html/body/div[4]")
    print(appid, "claimed")

def farm(accname):
    #modify this to suit your needs
    data = '''
    {
  "Enabled": true,
  "GamesPlayedWhileIdle": [
    730
  ],
  "RemoteCommunication": 0,
  "SteamLogin": "login",
  "SteamPassword": "password"
    }
'''
    jsonfile = json.loads(data)
    jsonfile["SteamLogin"] = accname
    jsonfile["SteamPassword"] = password
    archi = json.dumps(jsonfile, indent=2)
    trueloc = asflocation+"/config/"+accname+".json"
    with open(trueloc, "w") as f:
        f.write(archi)

