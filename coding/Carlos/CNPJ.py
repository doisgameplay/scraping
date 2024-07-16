from bs4 import BeautifulSoup
import requests
import re

url = "https://cnpj.biz/procura/maceio"
url = "https://cnpj.biz/procura/embraer"

def coletar_links(url):
    '''
    Aqui iremos coletar os links individuais dos sites das empresas e retornar uma lista
    '''
    links = []
    print('#'*50)
    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
        'Cookie' : 'XSRF-TOKEN=eyJpdiI6IjJ6OEhIWGtsTE5kYldFUlBNRFA2WWc9PSIsInZhbHVlIjoiMkpvTnBMZk9PNWxXaHpIM1E1WU5JMEVZS3VaNXBDME9oMm1RMkkrMHk1cGZ3WGlLaWpFV0UvRXRrdmNGVFRtWitKT2J4RUMxR0I3SzJDenpaTElBbDMzdU51cnVJUXFCbzVRWVhjSjdMRTNtU0d4ZU9BNEk3Tk9IRVNtRUdObXMiLCJtYWMiOiI3NzZlMmQ2MThiMmU0YTgyNzIwNTkxZjY2YWYwYmI2MmU2OTNmNDNhZGQ5NTE2MzgzOGE2MjMxZTQ0YzgwNGY5IiwidGFnIjoiIn0%3D; cnpj_biz_session=eyJpdiI6Ikd2OWtPTUlHbzVmVkVxc1p1QTNuQ1E9PSIsInZhbHVlIjoiYkJhSk1BR0MzM0tTOWlwNGR6ZjFEeEhVVjhrU1VndFJyaW9MRzB0TGxhNDhCK0ZBdTZJVUdxMFVpWjFuVDllaWRJWU4vRS9zck9tT0lqMEZqN0cvSUI5WndpMlNBSXZZVTBxNUUwUmx6Q1NreE9oODR1U1R1bTQwYTlpRHNLa3UiLCJtYWMiOiJiN2ZmZWQ0NWI4Mjc3OGQwMDFmNDg5ZDNiZTIwMDE3OWRhMzlhZWM3NjVlODA3ZGYxZGQ3MTU1N2Y0ZjIyMWY4IiwidGFnIjoiIn0%3D; cf_clearance=.XdUeEZoMaki_zgkmx559JL1BMZ2KuiN2dnMAdC7nFs-1721139840-1.0.1.1-9J43GIY8x.IPqO3auCixNYFJFvzwNIZKzzmAWe5WW3wjBpnIJazhKlOk73kon.e42E9yIS94bwRmMbq2YJgDzA'
    }

    page = requests.get(url, headers = headers)
    print(url, " RETORNOU ",page.status_code)
    soup = BeautifulSoup(page.text, "lxml")
    
    gray = soup.find_all('a', class_="block bg-gray-50 hover:bg-gray-100")
    white = soup.find_all('a', class_="block bg-white hover:bg-gray-100")
    informations = gray + white
    
    for info in informations:
        links.append(info['href'])
    
    return links

    
def coletar_informacoes_empresa(url):
    '''
    Aqui iremos coletar as informacoes da empresa
    '''

    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
        'Cookie' : 'XSRF-TOKEN=eyJpdiI6IlRyeEp2MlZOWlJjM05xMFlrRjF3YkE9PSIsInZhbHVlIjoiZW93Wmhsd1cyR0psMHo1S2FIbGdRQllKSU9NbHowcWVEZHlXa2pZUU5hcmhhT1RnWmU1U3ZUU3lqQ1FMcmFrbmRvUmwwQWI4c3IzOUR0WFc2ZVRiMm1YKzFuUzNGRkVuVHh0VS81MllLU3owdzdSZUJlTHJ3YlhFcVZhbU1RQVYiLCJtYWMiOiI0OGEyYWVmMjRjNzM3NTg5NThjNTk3NTQ5OThjYzA4NDA1YzEyMWVlN2U4MDVhODUxYzRjOTk5OTQyZDdmZDU4IiwidGFnIjoiIn0%3D; cnpj_biz_session=eyJpdiI6IjAwWGhlOUhNT3JuRlVFdnNWOXhpS3c9PSIsInZhbHVlIjoiNU9WUWREMlBKZUI0TkpPbjI5d3IxMkl6Z0ltNENCa2dDdEN3R29VYUxPeWcwSDRFdHBUNlZScVcxaXZ5WGRENytMeEQrR1JYS1d1SmhsRjVvT3NiTkdGVUhtNUNnelZRRzJTeitQbE9xUnRnSXhFakExc281T0x5S1hKK1VwRWkiLCJtYWMiOiI0NGI2ZTVmZDFjMWUyYTIyZmQzMzFlMjU5NzI0YzcyNjdjNjJmNWQ4ZDNjZGYzYWIyYjhkYTVlNzRiNDZlYmY0IiwidGFnIjoiIn0%3D; cf_clearance=.XdUeEZoMaki_zgkmx559JL1BMZ2KuiN2dnMAdC7nFs-1721139840-1.0.1.1-9J43GIY8x.IPqO3auCixNYFJFvzwNIZKzzmAWe5WW3wjBpnIJazhKlOk73kon.e42E9yIS94bwRmMbq2YJgDzA; _ga_ZBMG4K29EG=GS1.1.1721144324.1.0.1721144607.0.0.0; _ga=GA1.1.1411720590.1721144325; _gcl_au=1.1.1318858915.1721144325'
    }

    page = requests.get(url, headers = headers)
    print("¨"*50,f"\n\n{url} retornou {page.status_code}")
    
    if(page.status_code != 200):
        return     

    with open('doc.txt', 'a') as arquivo:
        soup = BeautifulSoup(page.text, 'lxml')
        nome_empresa = soup.find('h1', class_="post-title empresa-title").text.strip()
        informacoes = soup.find_all('b', class_="copy")
        for cu in informacoes:
            cus = cu.text.strip()
            if '(' in cus and '-' in cus and len(cus) <=15:
                arquivo.write(nome_empresa + ';' + cus + '\n')
                print(cus)

        

with open('doc.txt', 'w') as arquivo:
    arquivo.write("\n")

links = coletar_links(url)
for link in links:
    coletar_informacoes_empresa(link)


