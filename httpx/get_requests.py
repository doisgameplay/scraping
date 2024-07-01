#To put it shortly GET oftenn simply means: give me the documment located at URL

import httpx
response = httpx.get("https://httpbin.org/html")
metadata = response.headers  #headers da pagina 
html = response.text #pegando o html da pagina
print(response.status_code) #status_code retorna o codigo de resposta da pagina 
print(html)
print(metadata)


#We've already done a theoretical overview of requests headers and since they're
#so important in web scraping let's take a look at how we can use them with our 
#HTTP client:

response = httpx.get('http://httpbin.org/headers')
print(response.text)


#We can see that the client is generating teh required basics for us. To add so-
#me custom headers we can use the headers argument:

headers = {"User-Agent": "CUPINTO"}
response = httpx.get('http://httpbin.org/headers', headers=headers)
print(response.text)
