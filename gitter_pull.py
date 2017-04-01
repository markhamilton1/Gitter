# -*- coding: UTF-8 -*-
"""
gitter_pull.py
Version: 1.1.0
Created by: Mark Hamilton
Created: March 31, 2017
"""

from __future__ import print_function
import GithubSetup
import requests
import os
import string


try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3


def download():
    filename = 'gitter_pull.py'
    url = 'https://raw.githubusercontent.com/markhamilton1/Gitter/master/gitter_pull.py'
    __download_file(filename, url)


def __download_file(filename, url, directory='./'):
    print('\nGetting {} From GIT'.format(filename))
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        if r.encoding in ['ascii', 'utf-8']:
            with open(directory + filename, 'w') as file_fr:
                file_fr.write(r.text)
        else:
            with open(directory + filename, 'wb') as file_fr:
                file_fr.write(r.content)
        print('{} Downloaded Successfully'.format(filename))
    else:
        print('!{} Download Failed!'.format(filename))


def __get(prompt, default=None):
    input = raw_input(prompt).strip()
    if input == '':
        return default
    return input


def __get_repo_name():
    t = __get('Enter Repository Name:')
    return t


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
    if repo and repo.permissions and repo.permissions.pull:
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
        if repo.permissions.push:
            print(u"Access         : Writable")
        else:
            print(u"Access         : Read-Only")
        if repo.html_url:
            print(u"Github URL     : {}".format(repo.html_url))
        print()


def __pull(repo, rootdir, contents):
    for obj in contents:
        path = obj.path
        dir = os.path.dirname(path)
        curdir = rootdir
        if curdir[-1] != os.path.sep:
            curdir += os.path.sep
        curdir += dir
        if curdir[-1] != os.path.sep:
            curdir += os.path.sep
        if not os.path.exists(curdir):
            os.mkdir(curdir)
        file = os.path.basename(path)
        type = obj.type
        if type == 'file':
            if obj.size < 1000000:
                if obj.raw_data:
                    url = obj.raw_data[u"download_url"]
                else:
                    url = obj.download_url
                __download_file(file, url, curdir)
            else:
                print("\n{}".format(file))
                print("!File Too Big!")
        elif type == 'dir':
            dir_contents = repo.get_contents(path)
            __pull(repo, rootdir, dir_contents)


def pull_repo(gh, name):
    if name:
        query = "{} in:fullname".format(name)
        try:
            repos = gh.search_repositories(query)
        except:
            repos = None
        print()
        if repos and repos.totalCount > 0:
            if repos.totalCount > 1:
                print("Multiple Repositories Found")
                print()
                for repo in repos:
                    __print_repo_info(repo)
            else:
                repo = repos[0]
                contents = repo.get_contents("")
                parts = name.split('/')
                project_name = parts[1]
                curdir = os.getcwd()
                i = string.rfind(curdir, "/Documents")
                if i != -1:
                    i += len(os.path.sep + "Documents")
                    curdir = curdir[0:i]
                if curdir[-1] != os.path.sep:
                    curdir += os.path.sep
                dirpath = curdir + project_name + os.path.sep
                __pull(repo, dirpath, contents)
        else:
            print("Nothing Found")
    else:
        print("Pull Cancelled")
                    

if __name__ == "__main__":

    gh = __init_github()
    name = __get_repo_name()
    get_pull_repo(gh, name)
