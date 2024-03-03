import requests
access_token='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'
headers = {'Authorization': f'token {access_token}'}

def get_license_details(owner, repo):
    api_url = f'https://api.github.com/repos/{owner}/{repo}'
    response = requests.get(api_url,headers=headers)
    #Success
    if response.status_code == 200:
        result= response.json()
        if(result['license']):
          print(result['license'])
          return True
        else:
          print("No License")
          return False
    else:
        print(f"Error: Unable to retrieve license. Status code: {response.status_code}")
        return None

def get_profile_creation_date(username):
    profile_url = f'https://api.github.com/users/{username}'
    response = requests.get(profile_url,headers=headers)
    if response.status_code == 200:
        profile_data = response.json()
        return profile_data['created_at']
    else:
        return None

def get_total_repos(username):
    profile_url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(profile_url,headers=headers)
    if response.status_code == 200:
        profile_data = response.json()
        return len(profile_data)
    else:
        return None
def get_total_pulls(owner, repo):
    # API endpoint for getting commits
    access_token='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'
    headers = {'Authorization': f'token {access_token}'}
    counter=1
    while (1):
      api_url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{counter}'

      response = requests.get(api_url,headers=headers)
      #Success
      if response.status_code == 200:
          pulls = response.json()
          #print(pulls)
          total_commits=len(pulls)
          counter+=1
      else:
         # print(f" {response.status_code}")
          return counter-1

def get_commits(owner,repo):
   api_url = f'https://api.github.com/repos/{owner}/{repo}/commits'
   response = requests.get(api_url,headers=headers)
    #Success
   if response.status_code == 200:
        data= response.json()
        return len(data)
   else :return None

def get_repo_creation_date(owner,repo):
   api_url = f'https://api.github.com/repos/{owner}/{repo}'
   response = requests.get(api_url,headers=headers)
    #Success
   if response.status_code == 200:
        data= response.json()
        return data['created_at']
   else :return None
        
def get_total_Results(owner, repo):
    license=get_license_details(owner,repo)
    print('License Present :',license)
    creationDate=get_repo_creation_date(owner,repo)
    print(f'Repo {repo} Created at on {creationDate}')
    totalPulls=get_total_pulls(owner,repo)
    print(f'Total Pulls in {repo} are {totalPulls}')
    totalCommits=get_commits(owner,repo)
    print(f'Total Commits in {repo} are {totalCommits}')
    repolist={'name':repo,'owner':owner,'totalCommits':totalCommits,'totalPullRequests':totalPulls,'Created':creationDate,'license_Status':license}
    print(repolist)
    api_url = f'https://api.github.com/repos/{owner}/{repo}/contributors'
    response = requests.get(api_url,headers=headers)
    #Success
    if response.status_code == 200:
        data= response.json()
        contributors_list = []
        for contributor in data:
            username = contributor['login']
            contributions = contributor['contributions']
            profile_creation_date = get_profile_creation_date(username)
            total_repo=get_total_repos(username)
            contributors_list.append({
                'username': username,
                'contributions': contributions,
                'profile_creation_date': profile_creation_date,
                'total_repos':total_repo
            })

        # Print the result
        for contributor in contributors_list:
            print(f"{contributor['username']}: {contributor['contributions']} contributions, Profile created on {contributor['profile_creation_date']}, Total Repos are {contributor['total_repos']}")
    else:
        print(f"Error: Unable to retrieve commits. Status code: {response.status_code}")
    return (repolist,contributors_list)
# public repository
owner = 'jeremylong'
repo = 'DependencyCheck'
total_Results = get_total_Results(owner, repo)