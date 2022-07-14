 #!/usr/bin/python
 #################################
    #Name: Everlyne 
    #Date: 10/06/2022
    #SCRAPPING
# import imp
import requests

from bs4 import BeautifulSoup as bs
user_name = "Everlyne22"    #input your username
URL = "https://github.com"  + user_name  #input the site URL e.g instagram, facebook
results = requests.get(URL)

soup = bs(results.content,  "html.parser")
profile_photo = soup.find("img", {'alt' : 'Avatar'}) ['src']
print(profile_photo)
 