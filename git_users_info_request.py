import requests
import os
import json
import pandas
import csv

file = csv.reader(open("parsed_usernames_data/git_usernames.csv"), delimiter = ",")

file = list(file)

f = open("api_key", "r")
api_key = f.read()
f.close()

f = open("username", "r")
id_ = f.read()
f.close()

github_session = requests.Session()
github_session.auth = (id_, api_key)

if not os.path.exists("json_files_git_user_info"):
	os.mkdir("json_files_git_user_info")

for i in range (1, 641):
	username = file[i][1]
	response = json.loads(github_session.get("https://api.github.com/users/" + username).text)
	f = open("json_files_git_user_info/" + username + ".json", "w")
	f.write(json.dumps(response))
	f.close()
	


