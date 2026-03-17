import requests
import time 
import sys 
from concurrent.futures import ThreadPoolExecutor
import argparse

if len(sys.argv) < 3:
    print("Uso: python teste.py www.teste.com/DESTROY wordlist.txt ")
    exit()

host = sys.argv[1]
wordlist = sys.argv[2]
total = 0
t = 40
with open(wordlist, "r") as f:
    payloads = [linha.strip() for linha in f if linha.strip()]
    

def destroy(payload):
        r = requests.get(f"{host.replace("DESTROY", payload)}")
        if r.status_code == 200:
            print(f"\033[92m{host.replace('DESTROY', payload)}      STATUS:{r.status_code}\033[92m | LENGTH: {len(r.text)} | RESPONSE_TIME:{r.elapsed.total_seconds()}s")
        else:
            print(f"\033[91m {host.replace('DESTROY', payload)}      STATUS:{r.status_code}| LENGTH: {len(r.text)} | RESPONSE_TIME:{r.elapsed.total_seconds()}s")

           

       
with ThreadPoolExecutor(max_workers=t) as executor:
            executor.map(destroy, payloads)