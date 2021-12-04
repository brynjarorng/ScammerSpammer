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

proxies = {
"http": '5.186.155.151:21520',
"http": '78.156.109.221:14003',
"http": '176.20.154.49:10789',
"http": '37.97.23.100:63642',
"http": '176.20.154.49:17613',
"http": '95.154.20.222:26414',
"http": '95.154.20.222:22134',
"http": '37.97.23.100:17398',
"http": '95.154.20.222:33145',
"http": '84.238.33.155:10200',
"http": '5.186.155.151:53135',
"http": '5.186.155.151:22988',
"http": '37.97.23.100:61737',
"http": '95.154.20.222:19173',
"http": '176.20.154.49:47478',
"http": '95.154.20.222:31318',
"http": '176.20.154.49:57368',
"http": '176.20.154.49:52353',
"http": '178.157.228.96:19547',
"http": '176.20.154.49:52678',
"http": '5.103.137.240:1080',
"http": '185.89.43.41:1085',
"http": '93.176.85.240:39309',
"http": '93.164.33.114:41028',
"http": '185.89.42.53:1085',
"http": '5.103.139.93:1080',
"http": '185.89.42.91:1085',
"http": '89.239.212.208:1080',
"http": '45.159.115.62:1080',
"http": '80.63.107.91:4145',
"http": '185.89.43.225:1085',
"http": '45.159.115.60:1080',
"http": '185.89.42.102:1085',
"http": '77.68.237.158:47566',
"http": '93.163.52.152:4145',
"http": '87.60.31.9:4145',
"http": '93.167.67.69:4145',
"http": '185.89.42.47:1085',
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

        response = requests.post(url, headers=headers, cookies=cookies, files=files ,proxies=proxies)
        print(response.content)


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

chill()
#send_them_to_mars()