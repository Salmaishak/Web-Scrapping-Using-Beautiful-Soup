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

#create a tag object

#view the tag object type