import requests

api_url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000&country=all"

def get_proxy_list():
    response = requests.get(api_url)
    if response.status_code == 200:
        proxy_list = response.text.split('\n')
        return proxy_list
    else:
        return None

# Пример использования:

proxies = get_proxy_list()
if proxies:
    print(f"Найдено {len(proxies)} прокси-серверов: ")
    for proxy in proxies:
        print(proxy)
else:
    print("Не удалось загрузить список прокси-серверов.")
