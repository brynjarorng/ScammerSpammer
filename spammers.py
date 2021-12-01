import time
import csv
import random
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

names = []
with open("names.csv", newline='') as f:
    for l in csv.reader(f, delimiter=','):
        names.append(l[0])

passwords = []
with open("passwords.csv", newline='') as f:
    for l in csv.reader(f, delimiter=','):
        passwords.append(l[0])


address = "https://supportdanmarkstekniskeuniversitet.moonfruit.com/"
post_address = "https://secure.sitemakerlive.com/_form/submit"



# Fields to target
name_field = "ByAg5riaXYK"
email_field = "SJJW9HopXYt"
dtu_username = "rJIBQDoamFF"
password_field = "rkQwiTmYt"
alternative_email_field = "SkMvjT7Kt"
alternative_password_field = "r1-vs6mKF"
birthday_field = "r1KLjp7Kt"
state = "rywIo6mYF"

button= "/html/body/div[1]/div[1]/section/div/div[2]/div/form/div[10]/button"

state_options = ["student", "phd", "masters", "bachelor", "part-time", "full-time", "working and studying", "studying", "employer", "Spain", "Portugal", "Greece", "Italy", "Denmark", 
"Naerum", "Copenhagen", "Lisbon", "Sydney", "Alasca", "Alequente", "Buenos-Aires", "Borussia", "Germany", "Lyngby", "single", "married", "Single", "Married", "Engaged", "engaged"]



for i in range(100000000):
    browser = webdriver.Chrome()
    browser.get(address)

    # Chose a name, generate an email for dtu as well as a random username
    f_name = random.choice(names)
    m_name =str(random.choice([ " " + str(random.choice(names)), "", "", ""]))
    l_name = random.choice(names)
    s_id = "s" + random.choice(["19", "20", "21"]) + str(random.randrange(1000,9999))

    # Get random date
    start_date = datetime.date(1980, 5, 4)
    end_date = datetime.date(2001, 8, 6)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)

    random_date = start_date + datetime.timedelta(days=random_number_of_days)



    browser.find_element(By.NAME, name_field).send_keys(f_name + m_name + " " + l_name)
    browser.find_element(By.NAME, email_field).send_keys(s_id + "@student.dtu.dk")
    browser.find_element(By.NAME, dtu_username).send_keys(s_id)
    browser.find_element(By.NAME, password_field).send_keys(random.choice(passwords))
    browser.find_element(By.NAME, alternative_email_field).send_keys(f'{f_name.lower()}{random.randrange(0, 99)}@{random.choice(["gmail.com", "outlook.com", "hotmail.com", "live.com", "sapo.pt"])}')
    browser.find_element(By.NAME, alternative_password_field).send_keys(random.choice(passwords))
    browser.find_element(By.NAME, birthday_field).send_keys(str(random_date))
    browser.find_element(By.NAME, state).send_keys(random.choice(state_options))

    browser.find_element(By.XPATH, button).click()
    # TODO: add post

    time.sleep(2)

browser.quit()
