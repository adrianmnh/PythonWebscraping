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



driver.get(f'https://cssa.cunyfirst.cuny.edu/psc/cnycsprd/EMPLOYEE/CAMP/c/SA_LEARNER_SERVICES.SSR_SSENRL_SWAP.GBL?Page=SSR_SSENRL_SWAP&Action=A&ACAD_CAREER=UGRD&EMPLID={keys["id"]}&ENRL_REQUEST_ID=&INSTITUTION=QNS01&STRM=1222')

driver.execute_script("document.body.style.zoom='50%'")

username = driver.find_element(By.ID, "CUNYfirstUsernameH")
username.clear()
username.send_keys(keys["user"])
password = driver.find_element(By.ID, "CUNYfirstPassword").send_keys(keys["pword"])
driver.find_element(By.XPATH, '//*[@id="submit"]').click()

time.sleep(3)


while status:


    time.sleep(1)

    # different ways of selecting from a drop-down list
    classToChange =  driver.find_element(By.XPATH, '//*[@id="DERIVED_REGFRM1_DESCR50$225$"]/option[1]').click()

    element = driver.find_element(By.XPATH, '//*[@id="DERIVED_REGFRM1_SSR_CLASSNAME_35$183$"]')
    desiredClass =  Select(element)
    desiredClass.select_by_value("47254")

    time.sleep(1)

    submit = driver.find_element(By.XPATH, '//*[@id="DERIVED_REGFRM1_SSR_PB_ADDTOLIST1$184$"]').click()

    counter += 1
    print(f'***************************************Submission {counter}***************************************')

    time.sleep(2)

    submit = driver.find_element(By.ID, "DERIVED_REGFRM1_SSR_PB_SUBMIT").click()

    time.sleep(5)

    # find the success status from the image used
    result = driver.find_element(By.XPATH, '//*[@id="win0divDERIVED_REGFRM1_SSR_STATUS_LONG$0"]/div/img')

    time.sleep(1)
    image_url = result.get_attribute("src")
    Pattern = re.compile(".+ERROR.+")

    time.sleep(5)

    num = random.randrange(15)

    if Pattern.fullmatch(image_url) != None:
        print(f'Continue... waiting {num} seconds')
        driver.get(f'https://cssa.cunyfirst.cuny.edu/psc/cnycsprd/EMPLOYEE/CAMP/c/SA_LEARNER_SERVICES.SSR_SSENRL_SWAP.GBL?Page=SSR_SSENRL_SWAP&Action=A&ACAD_CAREER=UGRD&EMPLID={keys["id"]}&ENRL_REQUEST_ID=&INSTITUTION=QNS01&STRM=1222')
    else:
        status = False
        print(" _____ _   _ _____  _____  _____ _____ _____ _ ")
        print("/  ___| | | /  __ \/  __ \|  ___/  ___/  ___| |")
        print("\ `--.| | | | /  \/| /  \/| |__ \ `--.\ `--.| |")
        print(" `--. \ | | | |    | |    |  __| `--. \`--. \ |")
        print("/\__/ / |_| | \__/\| \__/\| |___/\__/ /\__/ /_|")
        print("\____/ \___/ \____/ \____/\____/\____/\____/(_)")
        
    time.sleep(num)
