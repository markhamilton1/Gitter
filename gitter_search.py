# -*- coding: UTF-8 -*-


from __future__ import print_function
import GithubSetup
from datetime import datetime


try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3


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
