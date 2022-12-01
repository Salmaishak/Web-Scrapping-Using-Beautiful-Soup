try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

# to search
query = "Steigenberger Hotel El Tahrir"
var =""
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
	if "booking"in j:
		var=j

print (var)

