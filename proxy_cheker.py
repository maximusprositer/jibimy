import requests

import socket


with open('proxy_list.txt', 'r') as file:

    proxies = file.readlines()



for proxy in proxies:
    proxy = proxy.strip() # удалить пробелы и символы переноса строки
  
  
    try:
        
        socket_proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        socket_proxy.settimeout(5)
        host, port = proxy.split(':')
        
        socket_proxy.connect((host, int(port)))

        socket_proxy.close()

        

        response = requests.get('https://www.google.com/', proxies={'https': f'https://{proxy}/'})

        if response.status_code == 200:

            print(f"Working proxy: {proxy}")
        
        else:
            
        print(f"Not working proxy: {proxy}")
 
   
        except:

        print(f"Not working proxy: {proxy}")
