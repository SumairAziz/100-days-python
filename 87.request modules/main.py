import requests 
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h1"):
  print(heading.text)


# data={
#     "title":"harry",
#     "body":"bhai",
#     "userId":12
# }

# headers={
#     "content-type":"application/json;charset=UTF-8"
# }

# response=requests.post(url,headers=headers,json=data)