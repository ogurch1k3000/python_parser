import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
browser.open("http://httpbin.org/")
browser.follow_link("forms")
browser.select_form('form[action="/post"]')

response = browser.submit_selected()
print(response.text)