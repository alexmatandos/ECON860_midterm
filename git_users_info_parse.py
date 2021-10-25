import os
import json
import pandas
import glob

if not os.path.exists("git_users_info_data"):
	os.mkdir("git_users_info_data")

df = pandas.DataFrame()

for file in glob.glob("json_files_git_user_info/*.json"):
	f = open(file, "r")
	json_data = json.load(f)
	f.close()
	
	df = df.append({
		'Username': json_data['login'],
		'ID Number': json_data['id'],
		'Node ID': json_data['node_id'],
		'Avatar URL': json_data['avatar_url'],
		'URL': json_data['html_url'],
		'Number of Followers': json_data['followers'],
		'Number of Following': json_data['following'],
		'Number of Starred': json_data['starred_url'],
		'Number of Gists': json_data['public_gists'],
		'Number of Repositories': json_data['public_repos'],
		'Name': json_data['name'],
		'Company': json_data['company'],
		'Blog': json_data['blog'],
		'Location': json_data['location'],
		'Email': json_data['email'],
		'Hireable': json_data['hireable'],
		'Biography': json_data['bio'],
		'Began in': json_data['created_at'],
		'Last Update': json_data['updated_at']
		}, ignore_index = True)

df.to_csv("git_users_info_data/git_users_info.csv")