import time
from random import randint, randrange
from datetime import datetime
import pytz
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def find_element_by_XPATH(xpath, driver, failed):
    delay = 15
    try:
        element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element
    except:
        print("Could not find element")
        failed = True
        return

def failedCheck(failed):
    if failed:
        initate_edusafe()
        return

def initate_edusafe():
    failed = False
    driver = webdriver.Chrome()
    driver.get("https://www.edusafe.io/login")

    emailElement = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]", driver, failed)
    failedCheck()

    email = "allenn@albertcollege.ca"
    for i in email:
        emailElement.send_keys(i)
        randNum = randrange(20)
        ranDelay = (randNum - 10) / 1000
        time.sleep(0.05 + ranDelay)

    passwordElement = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]", driver, failed)
    failedCheck()

    password = "Ngen10HK583"
    for i in password:
        passwordElement.send_keys(i)
        randNum = randrange(20)
        ranDelay = (randNum - 10) / 1000
        time.sleep(0.05 + ranDelay)

    loginButton = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/button[1]/span[1]", driver, failed)
    failedCheck()
    loginButton.click()

while True:
    # Do thing here

    initate_edusafe()
    

    defaultTime = 86400
    randNum = randint(-720, 720)
    waitingTime = defaultTime + randNum

    TOR = pytz.timezone('America/Toronto')
    timeNowTOR = datetime.now(TOR)
    controlTimeTOR = timeNowTOR.replace(hour=7, minute=0, second=0, microsecond=0, day=29)

    # If ahead of 7am, value > 0, if behind of 7am, value < 0
    secondsDifference = (timeNowTOR-controlTimeTOR).total_seconds()
    if secondsDifference < 0:
        # Wait the absolute value of secondsDifference
        print("Waiting absolute, waiting time: " + str(waitingTime))
        waitingTime += abs(secondsDifference)
    elif secondsDifference > 0:
        # Minus the extra time
        waitingTime =- secondsDifference


    time.sleep(waitingTime)