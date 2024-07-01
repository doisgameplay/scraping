import requests
from parsel import Selector

url = "https://www.remotepython.com/jobs/"
    


page = requests.get(url)

assert page.status_code == 200

selector = Selector(text=page.text)
for job in selector.css('.box-list .item'):
    title = job.css('h3 a::text').get()
    relative_url = job.css('h3 a::attr(href)').get()
    print(title)
    print("-"*50)








