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
    failedCheck(failed)

    email = "allenn@albertcollege.ca"
    for i in email:
        emailElement.send_keys(i)
        randNum = randrange(20)
        ranDelay = (randNum - 10) / 1000
        time.sleep(0.05 + ranDelay)

    passwordElement = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]", driver, failed)
    failedCheck(failed)

    password = "Ngen10HK583"
    for i in password:
        passwordElement.send_keys(i)
        randNum = randrange(20)
        ranDelay = (randNum - 10) / 1000
        time.sleep(0.05 + ranDelay)

    time.sleep(0.3)

    loginButton = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/button[1]/span[1]", driver, failed)
    failedCheck(failed)
    loginButton.click()

    time.sleep(0.3)

    startButton = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]", driver, failed)
    failedCheck(failed)
    startButton.click()

    time.sleep(0.3)

    yesButton = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]/span[1]", driver, failed)
    failedCheck(failed)
    yesButton.click()

    time.sleep(0.3)

    noButton = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]", driver, failed)
    failedCheck(failed)
    noButton.click()

    time.sleep(0.3)

    noButtonTwo = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]/span[1]", driver, failed)
    failedCheck(failed)
    noButtonTwo.click()

    time.sleep(0.3)

    noButtonThree = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]/span[1]", driver, failed)
    failedCheck(failed)
    noButtonThree.click()

    time.sleep(0.3)

    noButtonFour = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]/span[1]", driver, failed)
    failedCheck(failed)
    noButtonFour.click()

    time.sleep(0.3)

    noButtonFive = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]/span[1]", driver, failed)
    failedCheck(failed)
    noButtonFive.click()

    time.sleep(0.3)

    noButtonSix = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]/span[1]", driver, failed)
    failedCheck(failed)
    noButtonSix.click()

    time.sleep(0.3)

    noButtonSeven = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]/span[1]", driver, failed)
    failedCheck(failed)
    noButtonSeven.click()

    time.sleep(0.3)

    noButtonEight = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]/span[1]", driver, failed)
    failedCheck(failed)
    noButtonEight.click()

    time.sleep(0.3)

    noButtonNine = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]/span[1]", driver, failed)
    failedCheck(failed)
    noButtonNine.click()

    time.sleep(0.3)

    noButtonTen = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]/span[1]", driver, failed)
    failedCheck(failed)
    noButtonTen.click()

    time.sleep(0.3)

    noButtonEleven = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]/span[1]", driver, failed)
    failedCheck(failed)
    noButtonEleven.click()

    time.sleep(0.3)

    noButtonTwelve = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]/span[1]", driver, failed)
    failedCheck(failed)
    noButtonTwelve.click()

    time.sleep(0.3)

    okButton = find_element_by_XPATH("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/button[1]", driver, failed)
    failedCheck(failed)
    okButton.click()
    time.sleep(5)
    driver.quit()

while True:
    # Do thing here

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

    print("Waiting {} seconds for next edusafe action, randomized time: {}",waitingTime, randNum)

    if waitingTime > 0:
        time.sleep(waitingTime)

    initate_edusafe()