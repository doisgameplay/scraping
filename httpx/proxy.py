import httpx

proxies = {
    'http://': 'http://111.22.33.44:8500',
    'https://': 'http://111.22.33.44:8500'
}

response = httpx.get("http://httpbin.org/ip", proxies=proxies)
print(response.text)



