from urllib.request import urlopen
url = 'https://toscrape.com/'
page = urlopen(url)
f = open("result.txt", 'w')
f.write(page.read().decode('utf-8'))
f.close()