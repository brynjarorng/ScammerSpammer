import time
import csv
import random
import datetime
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

#Mode to run
MODE = ''
counter = 0

names = []
with open("data/names.csv", newline='') as f:
    for l in csv.reader(f, delimiter=','):
        names.append(l[0])

passwords = []
with open("data/passwords.csv", newline='') as f:
    for l in csv.reader(f, delimiter=','):
        passwords.append(l[0])

#Target address for using selenium
address = "https://supportdanmarkstekniskeuniversitet.weebly.com/"

#Target address for using request
post_address = "https://secure.sitemakerlive.com/_form/submit"


# Fields names to target
name_field = "ByAg5riaXYK"
email_field = "_u775833441838287881"
dtu_username = "rJIBQDoamFF"
password_field = "_u127872288731110885"
alternative_email_field = "_u698974889672718481"
alternative_password_field = "_u187973938768131043"
birthday_field = "_u979731754128240284"
state = "rywIo6mYF"

# Selenium button
button= "/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/form/div[3]/a/span"

def tab_changer(browser):
    global counter
    counter += 1
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[counter])

def runner_selenium():
    global MODE
    browser = webdriver.Chrome()
    while True:
    #TODO Add user agent
        
        browser.get(address)

        # Generate name , first middle last and full
        f_name = random.choice(names)
        m_name =str(random.choice([ " " + str(random.choice(names)), "", "", ""]))
        l_name = random.choice(names)
        full_name = f_name + m_name + " " + l_name

        # Generate random ID
        s_id = "s" + random.choice(["19", "20", "21"]) + str(random.randrange(1000,9999))

        # Generate random birthday date
        start_date = datetime.date(1980, 5, 4)
        end_date = datetime.date(2001, 8, 6)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        birthday = start_date + datetime.timedelta(days=random_number_of_days)

        #Generate random email
        email = f'{f_name.lower()}{random.randrange(0, 99)}@{random.choice(["gmail.com", "outlook.com", "hotmail.com", "live.com", "sapo.pt"])}'

        #browser.find_element(By.NAME, name_field).send_keys(full_name)
        browser.find_element(By.NAME, email_field).send_keys(s_id + "@student.dtu.dk")
        #browser.find_element(By.NAME, dtu_username).send_keys(s_id)
        browser.find_element(By.NAME, password_field).send_keys(random.choice(passwords))
        browser.find_element(By.NAME, alternative_email_field).send_keys(email)
        browser.find_element(By.NAME, alternative_password_field).send_keys(random.choice(passwords))
        browser.find_element(By.NAME, birthday_field).send_keys(str(birthday))

        browser.find_element(By.XPATH, button).click()

        if (MODE=="chill"):
            time.sleep(random.uniform(1,5))

def chill():
    global MODE
    MODE = "chill"
    runner_selenium()

#
def send_them_to_mars():
    global MODE
    MODE = "Mars"
    NUMBER_OF_THREADS = 10
    threads = []

    for i in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=runner_selenium)
        t.daemon = True
        threads.append(t)
    
    for i in range(NUMBER_OF_THREADS):
        threads[i].start()
    
    for i in range(NUMBER_OF_THREADS):
        threads[i].join()

#chill()
send_them_to_mars()
