import requests
import time 
import sys 
from concurrent.futures import ThreadPoolExecutor
import argparse

parser = argparse.ArgumentParser(description="Web fuzzer like ffuf")
parser.add_argument("-u", help="Target URL with DESTROY keyword")
parser.add_argument("-w", help="Wordlist file")
parser.add_argument("-t", type=int, default=50, help="(50 default) Number of threads")
parser.add_argument("--only-200", action="store_true", help="Show only 200 responses")
parser.add_argument("--length", default=None, type=int, help="length of response")
parser.add_argument("--mode", choices=["dns", "host"], default="dns")
parser.add_argument("--http", action="store_true", help="use if site is http only")
parser.add_argument("--timeout", type=int, default=5)
args = parser.parse_args()


base = args.u.replace("DESTROY.", "")
timeout = args.timeout
scheme = "http" if args.http else "https"


with open(args.w, "r") as f:
    payloads = [linha.strip() for linha in f if linha.strip()]
    

def destroy(payload):

    host = args.u.replace("DESTROY", payload)
        
       
    try:
        if args.mode == "dns":
            url = f"{scheme}://{host}"
            r = requests.get(url, timeout=5)

        elif args.mode == "host":
            url = f"{scheme}://{base}"

            r = requests.get(
                url,
                headers={"Host": host},
                timeout=5
            )

    except requests.exceptions.RequestException:
        return
    length = len(r.content)
    
    if args.length is not None and length != args.length:
        return
    if r.status_code == 200:
        print(f"\033[92m{host}      STATUS:{r.status_code}\033[92m | LENGTH: {length} | RESPONSE_TIME:{r.elapsed.total_seconds()}s\033[0m")
    elif not args.only_200:
        print(f"\033[91m{host}      STATUS:{r.status_code}| LENGTH: {length} | RESPONSE_TIME:{r.elapsed.total_seconds()}s\033[0m")


           
       
with ThreadPoolExecutor(max_workers=args.t) as executor:
            executor.map(destroy, payloads)