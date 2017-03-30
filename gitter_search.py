# -*- coding: UTF-8 -*-


from __future__ import print_function
import GithubSetup
from datetime import datetime


try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3


def __build_repo_query(user, repo, lang, topic):
    q = ""
    if user:
        q += "user:" + user + " "
    if repo:
        q += "repo:\"" + repo + "\" "
    if lang:
        q += "language:" + lang + " "
    if topic:
        q += "topic:" + topic
    if q == "":
        return None
    return q.strip()


def __build_user_query(user):
    q = ""
    if user:
        q += user
    if q == "":
        return None
    return q.strip()


def __get(prompt):
    input = raw_input(prompt).strip()
    if input == '':
        return None
    return input


def __get_language():
    return __get('Enter Repo Language:')


def __get_repo():
    return __get('Enter Repo Name:')


def __get_search_type():
    return __get('Enter Type Of Search (user or repo):')


def __get_topic():
    return __get('Enter Repo Topic:')


def __get_user():
    return __get('Enter Github User:')


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
        user = __get_user()
        query = __build_user_query(user)
        users = gh.search_users(query)
        print()
        if users and users.totalCount > 0:
            for user in users:
                __print_user_info(user)
        else:
            print("Nothing Found")
    elif type == 'repo':
        user = __get_user()
        repo = __get_repo()
        lang = __get_language()
        topic = __get_topic()
        query = __build_repo_query(user, repo, lang, topic)
        repos = gh.search_repositories(query)
        print()
        if repos and repos.totalCount > 0:
            for repo in repos:
                __print_repo_info(repo)
        else:
            print("Nothing Found")
