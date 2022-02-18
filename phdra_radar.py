import requests
from bs4 import BeautifulSoup
import re, os
import json
import io

dir_path = os.path.dirname(os.path.realpath(__file__))
headers = {"User-Agent":"Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
url = 'https://www.autoscout24.it/lst/lancia/phedra?sort=age&desc=1&ustate=N%2CU&size=20&page=1&atype=C&fc=4&qry=&'
stringdel=',-\nPrezzo finale offerto al pubblico, comprensivo di IVA, non vincolato all’acquisto di un finanziamento, a permuta o rottamazione. Passaggio di proprietà e IPT esclusi.'


def save_db(data):
    with open(dir_path+"/phedraDB.json", 'w', encoding="utf-8" ) as file:
        file.write(json.dumps(data, ensure_ascii=False,indent=4))
        file.close()

def exist(data,id):
    for barcone in data["vendite"]:
        if barcone["id"] == id : return True
    return False

def check_clear_db(data):
    for name in data:
        if len(data["vendite"])>1000:
            del(data["vendite"][:100])


def startupCheck():
    if os.path.isfile(dir_path+"/phedraDB.json") and os.access(dir_path+"/phedraDB.json", os.R_OK):
        return True
    else:
        print ("Either file is missing or is not readable, creating file...")
        with io.open(os.path.join(dir_path, 'phedraDB.json'), 'w') as db_file:
            db_file.write(json.dumps({"vendite":[]}))

def radar():
    append =  False
    final = {"new":[]}
    startupCheck()
    with open(dir_path+"/phedraDB.json", encoding="utf-8") as f:
        data = json.load(f)
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
        
    barconi= soup.find_all('div', {'class' : 'cldt-summary-full-item'})
    

    for barcone in barconi:
        try:
            titolo= barcone.find('h2', {'class' : 'cldt-summary-version sc-ellipsis'}).text
        except:
            titolo= 'Lancia Phedra'
        info={
            'id': barcone.get('id').replace('li-',''),
            'href': barcone.find('a', href=True)['href'],
            'title' : titolo,
            'price': barcone.find('span', {'class' : 'cldt-price sc-font-xl sc-font-bold'}).text.replace(stringdel,'').replace(',-','').replace('\n',' ').strip(),
            'km': barcone.find('li', {'data-type' : 'mileage'}).text.replace('\n',''),
            'year': barcone.find('li', {'data-type' : 'first-registration'}).text.replace('\n',''),
            'place': barcone.find('span',{'class' : re.compile(r'summary-seller-contact-zip-city')}).text
        }
        if not exist(data,info["id"]):
            data["vendite"].append(info)
            final["new"].append(info)
            append= True

    if append:
        check_clear_db(data)
        save_db(data)
    
    return final["new"]
    
'''
def main():
    radar()

if __name__ == "__main__":
    main()   

'''

