import requests
import bs4
lib1 = "https://books.toscrape.com/"
lib2 = "https://quotes.toscrape.com/"
#result = requests.get("https://books.toscrape.com/")
#soup = bs4.BeautifulSoup(result.text, "html.parser")
#soup = bs4.BeautifulSoup(result.text, "html.parser")
#print(soup.head.script.get_text())
#print(soup.title.get_text())
#print(soup.select("h1"))
'''yield soup select div'''
#for item in soup.select("img"):
#    print(item.get("src"))
#    input("Press Enter to continue...")

result = requests.get(lib2)
soup = bs4.BeautifulSoup(result.text, "lxml")
#print(soup.select("div.quote"))

authors = set()
for item in soup.select(".author"):
    authors.add(item.get_text())
#print(authors)

quotes = set()
for item in soup.select(".text"):
    quotes.add(item.get_text())
#print(quotes)

toptags = set()
for item in soup.select(".tag-item"):
    toptags.add(item.get_text())
#print(toptags)

url = "https://quotes.toscrape.com/page/"
authors1 = set()
for page in range(1, 11):
    result = requests.get(url + str(page))
    soup = bs4.BeautifulSoup(result.text, "lxml")
    for item in soup.select(".author"):
        authors1.add(item.get_text())
print(sorted(authors1))