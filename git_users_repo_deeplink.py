import os
import json
import pandas
import glob
import requests

if not os.path.exists("json_git_users_repo"):
	os.mkdir("json_git_users_repo")

f = open("api_key", "r")
api_key = f.read()
f.close()

f = open("username", "r")
id_ = f.read()
f.close()

github_session = requests.Session()
github_session.auth = (id_, api_key)

for file in glob.glob("json_files_git_user_info/*.json"):
	f = open(file, "r")
	json_data = json.load(f)
	f.close()
	username = json_data['login']
	repo_link = json_data['repos_url']
	response = json.loads(github_session.get(repo_link).text)
	f = open("json_git_users_repo/" + username + ".json", "w")
	f.write(json.dumps(response))
	f.close()

df = pandas.DataFrame()

if not os.path.exists("git_users_repo_data"):
	os.mkdir("git_users_repo_data")

for file in glob.glob("json_git_users_repo/*.json"):
	f = open(file, "r")
	json_data_1 = json.load(f)
	json_data_1 = list(json_data_1)
	f.close()
	
	for i in range(len(json_data_1)):
		repo = json_data_1[i]['full_name']
		description = json_data_1[i]['description']
		
		df = df.append({
			'Username/Repository': repo,
			'Description': description
			}, ignore_index = True)

df.to_csv("git_users_repo_data/repo_dataset.csv")