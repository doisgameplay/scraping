import requests
from bs4 import BeautifulSoup


'''
page = requests.get(url)

#print(page.status_code)
#print(page.headers)

soup = BeautifulSoup(page.text, "lxml")
commentaries = soup.find_all('div', class_="testimonial")
for comment in commentaries:
    print(comment.text.strip())
    count += 1
'''
count = 0


url = "https://web-scraping.dev/api/testimonials"
page_number = 1
while(True):
    params = {'page' : page_number}
    headers = {
        'Referer':'https://web-scraping.dev/testimonials',
        'x-secret-token':'secret123'
    }


    page = requests.get(url, params = params, headers = headers)
    soup = BeautifulSoup(page.text, "lxml")
    commentaries = soup.find_all('div', class_="testimonial")
    if(commentaries == []):
        break
    print('-'*30)
    for comment in commentaries:
        print(comment.text.strip())
        count += 1

    page_number+=1








