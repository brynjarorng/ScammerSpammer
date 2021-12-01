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

address = "http://support-danmarkstekniskeuniversitet.moonfruit.com/"
post_address = "https://secure.sitemakerlive.com/_form/submit"

browser = webdriver.Chrome(executable_path="/home/brynjarog/selenium_chrome/drivers/chromedriver")

# Fields to target
name_field = "BJAgcCurdAH"
email_field = "rykWqA_B_CS"
password_field = "Bk2eYBOCH"
alternative_email_field = "HyFltSuAr"
alternative_password_field = "SkoclRmKF"
birthday_field = "Bycnl0mtK"


for i in range(3):
    browser.get(address)

    # Chose a name, generate an email for dtu as well as a random username
    f_name = random.choice(names)
    l_name = random.choice(names)
    s_id = "s" + random.choice(["19", "20", "21"]) + str(random.randrange(1000,9999))

    # Get random date
    start_date = datetime.date(1980, 5, 4)
    end_date = datetime.date(2001, 8, 6)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)

    random_date = start_date + datetime.timedelta(days=random_number_of_days)



    # browser.find_element(By.NAME, name_field).send_keys(f_name + " " + l_name)
    # browser.find_element(By.NAME, email_field).send_keys(s_id + "@student.dtu.dk")
    # browser.find_element(By.NAME, password_field).send_keys(random.choice(passwords))
    # browser.find_element(By.NAME, alternative_email_fielde_field).send_keys(f'{fname.lower()}{random.randrange(0, 99)}@{random.choice(["gmail.com", "outlook.com", "hotmail.com", "live.com", "sapo.pt"])}')
    # browser.find_element(By.NAME, alternative_password_field).send_keys(random.choice(passwords))
    # browser.find_element(By.NAME, birthday_field).send_keys(str(random_date))

    # TODO: add post


    time.sleep(1)


browser.quit()
