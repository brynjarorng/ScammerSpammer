import requests
import csv
import random
import datetime
import threading

names = []
with open("data/names.csv", newline='') as f:
    for l in csv.reader(f, delimiter=','):
        names.append(l[0])

passwords = []
with open("data/passwords.csv", newline='') as f:
    for l in csv.reader(f, delimiter=','):
        passwords.append(l[0])

user_agents = []
with open("data/user-agents.csv", newline='') as f:
    for l in csv.reader(f, delimiter=','):
        user_agents.append(l[0])

url = 'https://supportdanmarkstekniskeuniversitet.weebly.com/ajax/apps/formSubmitAjax.php'

cookies = {
    'language': 'en',
}

proxy = {
"http": 'https://193.163.116.14:1080',
"http": 'https://193.162.105.112:5678',
"http" :'https://193.163.116.30:1080' 
}

def chill():
    counter = 0
    while True:
        counter+=1
        f_name = random.choice(names)

        # Generate random ID
        s_id = "s" + random.choice(["19", "20", "21"]) + str(random.randrange(1000,9999))

        # Generate random birthday date
        start_date = datetime.date(1975, 5, 4)
        end_date = datetime.date(2001, 8, 6)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        birthday = start_date + datetime.timedelta(days=random_number_of_days)

        #Generate random email
        email = f'{f_name.lower()}{random.randrange(0, 99)}@{random.choice(["gmail.com", "outlook.com", "hotmail.com", "live.com", "sapo.pt", "connectdenmark.com", "forum.dk", "jubiipost.dk", "yahoo.com"])}'
        email_dtu = s_id + "@student.dtu.dk"
        
        files = {
            '_u775833441838287881': (None, email_dtu ),
            '_u127872288731110885': (None, random.choice(passwords)),
            '_u698974889672718481': (None, email),
            '_u187973938768131043': (None, random.choice(passwords)),
            '_u979731754128240284': (None, str(birthday)),
            'wsite_subject': (None, ''),
            'form_version': (None, '2'),
            'wsite_approved': (None, 'approved'),
            'ucfid': (None, '516641276899099204'),
            'recaptcha_token': (None, ''),
        }
        
        headers = {
        'User-Agent': random.choice(user_agents)
        }

        response = requests.post(url, headers=headers, cookies=cookies, files=files ,proxies=proxy)
        print(counter)


def send_them_to_mars():
    NUMBER_OF_THREADS = 50
    threads = []

    for i in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=chill)
        t.daemon = True
        threads.append(t)
    
    for i in range(NUMBER_OF_THREADS):
        threads[i].start()
    
    for i in range(NUMBER_OF_THREADS):
        threads[i].join()

#chill()
send_them_to_mars()