from urllib.request import urlopen
import re
url = 'https://toscrape.com/'
page = urlopen(url)
html_code = page.read().decode('utf-8')
link = r'(https?://\S+)(?=")'
print(re.findall(link, html_code))
