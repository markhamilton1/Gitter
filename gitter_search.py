# -*- coding: UTF-8 -*-
"""
gitter_search.py
Version: 1.0.0
Created by: Mark Hamilton
Created: March 30, 2017
gitter_search is a module that provides
basic search services in Pythonista for
Github.
gitter_search is implemented on the
Github API v3.
This API requires a username and password
to login to a Github account.
When you have a Github account, follow
these steps.
1. Execute gitter_search in Pythonista on
your iOS device.
2. Enter the username at the prompt.
3. Enter the password at the prompt.
If everything was completed successfully
you will then be prompted to choose the
type of search you want to do: user or
repo.
"""


from __future__ import print_function
import GithubSetup
from datetime import datetime


COMMON_USER_QUERIES = {
    '#poppy' : 'language:python repos:>=1 followers:>=1000'
}
COMMON_REPO_QUERIES = {
    '#poppy' : 'language:python stars:>=100',
    '#poppista' : 'language:python stars:>=10 topic:pythonista'
}


try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3


def download():
    print('\nGetting gitter_search.py From GIT')
    url = 'https://raw.githubusercontent.com/markhamilton1/Gitter/master/gitter_search.py'
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        with open('gitter_search.py', 'w') as script_fr:
            script_fr.write(r.text)
        print('gitter_search.py Downloaded Successfully')
    else:
        print('!gitter_search.py Download Failed!')
        

def __get(prompt, default=None):
    input = raw_input(prompt).strip()
    if input == '':
        return default
    return input


def __get_search_terms(search_type):
    while True:
        q = __get('Enter Search Terms (-h for help):')
        if q == '-h':
            print()
            print('To search enter the desired query and press return.')
            if search_type == 'user':
                print('For a detailed explanation of how to build a user')
                print('search query go to')
                print('https://developer.github.com/v3/search/#search-users')
            elif search_type == 'repo':
                print('For a detailed explanation of how to build a repo')
                print('search query go to')
                print('https://developer.github.com/v3/search/#search-repositories')
            print()
        else:
            if q.startswith('#'):
                if search_type == 'user':
                    try:
                        newq = COMMON_USER_QUERIES[q]
                        q = newq
                    except:
                        pass
                elif search_type == 'repo':
                    try:
                        newq = COMMON_REPO_QUERIES[q]
                        q = newq
                    except:
                        pass
            return q


def __get_search_type():
    t = __get('Enter Type Of Search ([user]|repo):', 'user')
    if t in ['repo', 'user']:
        return t
    return None


def __init_github():
    gh = GithubSetup.init('Gitter_Creds')
    if gh is None:
        username = GithubSetup.get_username()
        if username is not None and username != '':
            password = GithubSetup.get_password()
            if password is not None and password != '':
                gh = GithubSetup.init('Gitter_Creds', username, password)
        if gh is None:
            print('!Failed To Initialize Github Session!')
    return gh


def __print_repo_info(repo):
    if repo:
        print(u"Repository Name: {}".format(repo.full_name))
        if repo.owner:
            if repo.owner.name:
                print(u"Owner          : {}".format(repo.owner.name))
            else:
                print(u"Owner          : {}".format(repo.owner.login))
        if repo.created_at:
            print(u"Created        : {}".format(str(repo.created_at)))
        if repo.description:
            print(u"Description    : {}".format(repo.description))
        if repo.language:
            print(u"Language       : {}".format(repo.language))
        if repo.size:
            print(u"Size           : {}kb".format(repo.size))
        if repo.watchers_count:
            print(u"Watchers       : {}".format(repo.watchers_count))
        if repo.forks_count:
            print(u"Forks          : {}".format(repo.forks_count))
        if repo.open_issues_count:
            print(u"Open Issues    : {}".format(repo.open_issues_count))
        if repo.html_url:
            print(u"Github URL     : {}".format(repo.html_url))
        print()


def __print_user_info(user):
    if user:
        if user.name:
            print(u"User        : {}".format(user.name))
        else:
            print(u"User        : {}".format(user.login))
        if user.company:
            print(u"Company     : {}".format(user.company))
        if user.location:
            print(u"Location    : {}".format(user.location))
        if user.blog:
            print(u"Blog        : {}".format(user.blog))
        if user.email:
            print(u"Email       : {}".format(user.email))
        if user.public_gists:
            print(u"Public Gists: {}".format(user.public_gists))
        if user.public_repos:
            print(u"Public Repos: {}".format(user.public_repos))
        if user.followers:
            print(u"Followers   : {}".format(user.followers))
        if user.updated_at:
            print(u"Last Updated: {}".format(str(user.updated_at)))
        if user.html_url:
            print(u"Github URL  : {}".format(user.html_url))
        print()


if __name__ == "__main__":

    gh = __init_github()

    type = __get_search_type()
    if type == 'user':
        print('Github User Search --------------------------')
        query = __get_search_terms('user')
        users = gh.search_users(query)
        print()
        if users and users.totalCount > 0:
            for user in users:
                __print_user_info(user)
        else:
            print("Nothing Found")
    elif type == 'repo':
        print('Github Repo Search --------------------------')
        query = __get_search_terms('repo')
        repos = gh.search_repositories(query)
        print()
        if repos and repos.totalCount > 0:
            for repo in repos:
                __print_repo_info(repo)
        else:
            print("Nothing Found")
    else:
        print("Unrecognized Search Type")
