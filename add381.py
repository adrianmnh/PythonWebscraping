


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import re
import random
import json

status = True
counter = 0;
with open('keys.json') as f:
    keys = json.load(f)

#PATH = "./chromedriver.exe"
PATH = "C:\drivers\geckodriver.exe"

service = Service(PATH)
driver = webdriver.Firefox(service=service)
#driver = webdriver.Chrome(service=service)
driver.set_window_size(450, 650)
#driver.get("https://home.cunyfirst.cuny.edu/")



driver.get(f'https://cssa.cunyfirst.cuny.edu/psc/cnycsprd/EMPLOYEE/CAMP/c/SA_LEARNER_SERVICES.SSR_SSENRL_ADD.GBL?Page=SSR_SSENRL_ADD_C&Action=U&ACAD_CAREER=UGRD&EMPLID={keys["id"]}&ENRL_REQUEST_ID=0061938917&INSTITUTION=QNS01&STRM=1222&TargetFrameName=None')

driver.execute_script("document.body.style.zoom='50%'")

username = driver.find_element(By.ID, "CUNYfirstUsernameH")
username.clear()
username.send_keys(keys["user"])
password = driver.find_element(By.ID, "CUNYfirstPassword").send_keys(keys["pword"])
driver.find_element(By.XPATH, '//*[@id="submit"]').click()

time.sleep(3)


while status:


    time.sleep(1)

    submit = driver.find_element(By.XPATH, '//*[@id="DERIVED_REGFRM1_SSR_PB_SUBMIT"]').click()

    counter += 1
    print(f'***************************************Submission {counter}***************************************')

    time.sleep(5)

    # find the success status from the image used
    result = driver.find_element(By.XPATH, '//*[@id="win0divDERIVED_REGFRM1_SSR_STATUS_LONG$3"]/div/img')

    time.sleep(1)
    image_url = result.get_attribute("src")
    Pattern = re.compile(".+ERROR.+")

    time.sleep(5)

    num = random.randrange(15)

    if Pattern.fullmatch(image_url) != None:
        print(f'Continue... waiting {num} seconds')
        driver.get(f'https://cssa.cunyfirst.cuny.edu/psc/cnycsprd/EMPLOYEE/CAMP/c/SA_LEARNER_SERVICES.SSR_SSENRL_ADD.GBL?Page=SSR_SSENRL_ADD_C&Action=U&ACAD_CAREER=UGRD&EMPLID={keys["id"]}&ENRL_REQUEST_ID=0061938917&INSTITUTION=QNS01&STRM=1222&TargetFrameName=None')
    else:
        print("SUCCESS! Class swap was successful, you're now enrolled on CSCI 381 with Roday")
        print(" _____ _   _ _____  _____  _____ _____ _____ _ ")
        print("/  ___| | | /  __ \/  __ \|  ___/  ___/  ___| |")
        print("\ `--.| | | | /  \/| /  \/| |__ \ `--.\ `--.| |")
        print(" `--. \ | | | |    | |    |  __| `--. \`--. \ |")
        print("/\__/ / |_| | \__/\| \__/\| |___/\__/ /\__/ /_|")
        print("\____/ \___/ \____/ \____/\____/\____/\____/(_)")
        status = False


    time.sleep(num)
