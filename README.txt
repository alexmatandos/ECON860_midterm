README

(1) Execute 'git_usernames_request_parse.py' to request the html file from 'http://45.79.253.243/index.html' and parse through all the unique values for GitHub usernames contained inside. The 'git_usernames.csv' file will be generated inside the also generated folder 'parsed_usernames_data'.

(2) Execute 'git_users_info_request.py' to loop through each unique username contained in 'git_usernames.csv' and request the API files required for parsing the information. Creates the folder 'json_files_git_user_info' with the JSON files for each unique username. Disclaimer: to access GitHub's API you'll need to use your own personal API token and username.

(3) Execute 'git_users_info_parse.py' to loop through each unique JSON files and scrape the following information: Username, ID Number, Node ID, Avatar URL, URL, Number of Followers, Number of Following, Number of Starred, Number of Gists, Number of Repositories, Name, Company, Blog, Location, Email, Hireable, Biography, Began in, and Last Update. Generates the 'git_users_info.csv' file, inside the folder 'git_users_info' with all the compiled information.

(4) BONUS: Execute 'git_users_repo_deeplink.py' to return all the repositories for each username. Generates the folder 'json_git_users_repo' containing the JSON files for the repositories for each username and the folder 'git_users_repo_data' containing the file 'repo_dataset.csv' compiling all information.