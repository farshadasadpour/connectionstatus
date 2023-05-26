
from telnetlib import Telnet
from datetime import datetime
import config
import requests
import time
import socket
import os

def __telnet():
    host = os.getenv('host',socket.gethostname())
    if config.end_points:
        for server in config.end_points:
            try:
                for key, value in server.items():
                    # print(key,value)
                    for port in value:
                        with Telnet(
                            host=key,
                            port=int(port),
                            timeout=10
                        ) as tn:
                            # print(tn)
                            # print(f"{tn.get_socket()}")
                            success_json = {
                                "Connection": True,
                                "Server": str(key),
                                "Port": int(port),
                                "Machin": host,
                                "Date": datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                            }
                            print(f"success_json:{success_json}")
                            __logs(success_json)
            except Exception as a:
                failure_json = {
                    "Connection": False,
                    "Server": str(key),
                    "Port": int(port),
                    "Machin": host,
                    "Date": datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                }
                print(f"failure_json:{failure_json}")
                __logs(failure_json)
    else:
        exit()

def __logs(playload):
    elastic_url = os.getenv('elk_url')
    index_name = os.getenv('index_name')
    pipeline = os.getenv('pipeline','DateChanger')
    api_key = os.getenv('api_key')
    url = f'{elastic_url}/{index_name}/_doc?pipeline={pipeline}'
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    header = {
        "Authorization": f"ApiKey {api_key}",
        }
    try:
        response = requests.post(
            url=url,
            json=playload,
            headers=header,
            verify=False
        )
        print('response: ',response.text)
    except Exception as error:
        print('error: ',error)

if __name__ == '__main__':
    delay = int(os.getenv('delay',60))
    while True:
        time.sleep(delay)
        __telnet() 
