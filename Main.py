from bs4 import BeautifulSoup

html_doc= """<html>
<body>
<h1> MY NAME IS SALMA </h1>
<b>
<!--- this is a comment Line--></b>
<p title= "about me" class ="text"> 
my first paragraph</p>
<div class="cities">
<h2> london </h2>
</div>
</body>
</html>
"""

#parse it using html parser
soup = BeautifulSoup(html_doc, 'html.parser')
#view the type of soup object
print (type(soup))
#view the soup object
print (soup)
#create a tag object
tag = soup.p #we specified we want paragraph
#print the tag
print( tag)
# <p class="text" title="about me"> my first paragraph</p>

comment = soup.b.string
print(type(comment))
print(tag.attrs)
print (tag.string) #el gwa el paragraph

print(type(tag.string))