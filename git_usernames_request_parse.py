import urllib.request
import os
from bs4 import BeautifulSoup
import pandas

if not os.path.exists("parsed_usernames"):
	os.mkdir("parsed_usernames")

if not os.path.exists("html_files_git_usernames"):
	os.mkdir("html_files_git_usernames")

df = pandas.DataFrame()

f = open("html_files_git_usernames/TestServer.html", "wb")
response =  urllib.request.urlopen("http://45.79.253.243/index.html")
html = response.read()
f.write(html)
f.close()

f = open("html_files_git_usernames/TestServer.html", "r")
soup = BeautifulSoup(f.read(), "html.parser")
f.close()

table = soup.find("div", {"class": "grid grid-cols-3 gap-4"})

usernames = table.find_all("div")

for username in usernames:
	tag = username.get("ghid")

	df = df.append({
		"User Names": tag,
		}, ignore_index = True)

	df = df.drop_duplicates()

df.to_csv("parsed_usernames/git_usernames.csv")