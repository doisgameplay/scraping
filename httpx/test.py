import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0'}

page = requests.get('https://www.amazon.com/MARTHA-STEWART-Eastwalk-Stainless-Cutlery/dp/B0BNJWWR3S/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.5a1e43ac-8800-488a-812b-a43cf4218174&crid=IBML6MYDLJ4A&dib=eyJ2IjoiMSJ9.UgSPEWhPccYdve_XQ6q7Jj3hCjdhgwUjStQWZTzhCuCb-9rFzMScSoYN8Mev1nrsZntuSZjZ-2nb9TNrJJuGQ6OduDHzJNeNj623FS1VcRsxWbGJj6TYmrnHTcQJa7HUDOhPDqVlYXNnR2QrNBttckDa_WOJUlUJpYWoS8C8J-F8AXHQ2NB-cMZDTT5q5FtbblaXGS7G1hX9Cp1D4TP9McFNadjDeSNoc_8Cy8s41AAuFO16qhIQZ2NpCUDK1NxFOLCCWY21XQ6CN8ti9LLeGKfUH-Gup7O8ExJC4On-lqg.bGvc9xAEVDa5qAD5YxrO7n4KzuTOxlDHsVcWrAynp5c&dib_tag=se&keywords=Dinnerware%2B%26%2Baccessories&pd_rd_r=a827c4d1-8d50-4765-ba10-d85a7d2a9bbb&pd_rd_w=YpFEA&pd_rd_wg=aDyOO&pf_rd_p=5a1e43ac-8800-488a-812b-a43cf4218174&pf_rd_r=225ZZVWXFWFPQYXD7P81&qid=1719863614&sprefix=dinnerware%2B%26%2Baccessorie%2Caps%2C190&sr=8-1&th=1')


#print(page.text)
print(page.status_code)






