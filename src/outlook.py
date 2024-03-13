import time
import json
from random import randint
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from constants import password, driver, firstname, lastname, usrname


def create():
    random = randint(100000, 999999)

    username = usrname + str(random)
    driver.get("https://signup.live.com/?lic=1")
    liveswitch = driver.find_element(By.ID, "liveSwitch")
    liveswitch.click()
    mailbox = driver.find_element(By.ID, "MemberName")
    mailbox.send_keys(username + Keys.RETURN)
    time.sleep(2)
    passwd = driver.find_element(By.ID, "PasswordInput")
    passwd.send_keys(password + Keys.RETURN)
    firstn = driver.find_element(By.ID, "FirstName")
    lastn = driver.find_element(By.ID, "LastName")
    firstn.send_keys(firstname)
    lastn.send_keys(lastname + Keys.RETURN)
    month = driver.find_element(By.ID, "BirthMonth")
    day = driver.find_element(By.ID, "BirthDay")
    year = driver.find_element(By.ID, "BirthYear")

    Select(month).select_by_value("4")
    Select(day).select_by_value("1")

    year.send_keys("1990" + Keys.RETURN)
    print("waiting for captcha...")
    consent = driver.find_element(By.XPATH, "//span[contains(text(), 'OK')]")
    print("Captcha Solved!")
    consent.click()
    consent.click()
    consent.click()
    yes = driver.find_element(By.ID, "acceptButton")
    yes.click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Privacy & cookies")

    # temporary json for testing
    with open("../accounts.json", "a") as f:
        json.dump(username, f, indent=2)
        f.write("\n")

    return username


def verifysteam():
    driver.get("https://outlook.live.com/mail/0/")
    driver.find_element(By.XPATH, "//span[contains(text(), 'New Steam Account')]").click()
    driver.find_element(By.XPATH,
                        "//span[@class='x_link x_c-grey4' and contains(text(),'Verify My Email Address')]").click()
