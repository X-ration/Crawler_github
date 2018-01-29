#shell command install pygithub
#$pip install pygithub

#demo
from github import Github
# Specify your own access token here
ACCESS_TOKEN = ''
gh = Github(ACCESS_TOKEN)

repos = gh.get_repos()
repo_l_all = []
user_l_all = []
try:
    for i,repo in enumerate(repos):
        print 'collect',i
        repo_id = repo.id
        repo_name = repo.name
        repo_stars = repo.stargazers_count
        repo_forks = repo.forks_count
        repo_watches = repo.watchers_count
        user = repo.owner
        user_name = user.name
        user_id = user.id
        user_expr = user.created_at
        user_location = user.location
        user_company = user.company
        user_repos = user.public_repos
        repo_l_all.append(list((repo_id,user_id,repo_name,repo_stars,repo_forks,repo_watches)))
        print list((repo_id,user_id,repo_name,repo_stars,repo_forks,repo_watches))
        user_l_all.append(list((user_id,user_name,user_expr,user_location,user_company,user_repos)))
        print list((user_id,user_name,user_expr,user_location,user_company,user_repos))
except Exception,e:
    print "Collecting data encounters exception. Numbers of repos collected:",i
    print 'Exception:-->\n',e.message

#爬取完毕后，将数据存储到本地
import pandas as pd
df_repo = pd.DataFrame(repo_l_all, columns=['repo_id','user_id','repo_name','repo_stars','repo_forks','repo_watches'])
df_user = pd.DataFrame(user_l_all, columns = ['user_id','user_name','user_expr','user_location','user_company','user_repos'])
df_repo.to_csv("C:\\Users\\Frank\\Desktop\\github_repo.csv",encoding='utf-8')
df_user.to_csv("C:\\Users\\Frank\\Desktop\\github_user.csv",encoding='utf-8')
#得到repo_name,repo_star,repo_fork,repo_watch,
#repo_user_name,user_star,user_repos, user_followers, user_followings