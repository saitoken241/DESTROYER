import requests
import time 
import sys 
from concurrent.futures import ThreadPoolExecutor

if len(sys.argv) < 3:
    print("Uso: python teste.py www.teste.com/DESTROY wordlist.txt ")
    exit()

host = sys.argv[1]
wordlist = sys.argv[2]
total = 0
t = 10
with open(wordlist, "r") as f:
    payloads = [linha.strip() for linha in f if linha.strip()]
    

def destroy(payload):
        r = requests.post(f"{host.replace("DESTROY", payload)}")
        print(f"{host.replace('DESTROY', payload)}      STATUS:{r.status_code} | LENGTH: {len(r.text)} | RESPONSE_TIME:{r.elapsed.total_seconds()}s")
           

       
with ThreadPoolExecutor(max_workers=t) as executor:
            executor.map(destroy, payloads)