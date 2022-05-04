import requests
import os
import random
import json 
import time


def getCode(catchall,regione):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'content-type': 'application/json',

    }

    data = {
    "id":"06fe5b50b4218612aa3fa8494df326aef7ff35a75a8563b3455bb53c15168872","variables":{"input":{"email": catchall,"preference":{"category":"MEN","topics":[{"id":"item_alerts","isEnabled":bool(True)},{"id":"survey","isEnabled":bool(True)},{"id":"recommendations","isEnabled":bool(True)},{"id":"fashion_fix","isEnabled":bool(True)},{"id":"follow_brand","isEnabled":bool(True)},{"id":"subscription_confirmations","isEnabled":bool(True)},{"id":"offers_sales","isEnabled":bool(True)}]},"referrer":"nl_subscription_banner_one_click","clientMutationId":"1620930739401"}}


    }



    url =  "https://www.zalando."+str(regione)+"/api/graphql/"
    s = requests.Session()

    resp = s.post(url,headers=headers,json=data)

    ciao  = resp.json()

    email = ciao["data"]['subscribeToNewsletter']['isEmailVerificationRequired']

    if (email == False):
        print ("discount generated")

    else:print ("yooo WTF there was an error"+str(resp.status_code))

regione = input ('insert region(it,fr..): ')

quantita = input('insert quantity: ')

catchall = input('insert catchall(@123.com): ')

os.system('cls')

quantita = int(quantita)

nomi = ['Alessandro','Riccardo','Diego','Tommaso','Matteo','Lorenzo','Gabriele','Samuele','Giacomo','beatrice','sofia','ginevra','gaia']
cognomi=['Rossi','Ferrari','Russo','Bianchi','Romano','Gallo','Costa','Fontana','conti','esposito','ricci','bruno','greco']

i=0

while (i < quantita):

    num = random.randint(1111,9999)

    indice=random.randint(0,12)

    eml = (nomi[indice]+str(cognomi[indice])+str(num)+str(catchall))

    getCode(eml,regione)


    i+=1
time.sleep(2)
print ("finished")