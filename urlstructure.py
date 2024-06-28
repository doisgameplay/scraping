from urllib.parse import urlparse
url = 'https://scrapfly.io/blog/parsing-html-with-xpath/#what-is-xpath'
url = 'https://www.remotepython.com/jobs/'
url = 'https://web-scraping.dev/testimonials'
url = "https://web-scraping.dev/api/testimonials?page=2"
url = 'https://www.imdb.com/title/tt20918700/'
a = urlparse(url)

print(a)

