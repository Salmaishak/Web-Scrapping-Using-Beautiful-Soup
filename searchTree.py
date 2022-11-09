from bs4 import BeautifulSoup
HTMLfilePath="web_scraping_example.html"
with open(HTMLfilePath, "r") as organization:
    soup = BeautifulSoup(organization, "lxml")

print(soup.contents)
tag_p = soup.find("h2")
print(tag_p)
byID= soup.find(id= 'one')
print(byID)
print(byID.string)
#search for string only
searchForStrings = soup.find(text=["hello"])
print (searchForStrings)
#Strip string method
for string in soup.stripped_strings:
    print(repr(string))