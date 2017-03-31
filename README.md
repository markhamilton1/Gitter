# Gitter
Basic Github support for Pythonista. (Pythonista)
Gitter will eventually consist of a number of Github tools for use in Pythonista.

To use this functionality you must install PyGithub. I recommend using the stash
shell with the command: `pip install PyGithub`. All of the Gitter functionality
is dependent on this package that provides access to the Giyhub APIs.

gitter_search is a module that provides basic search services in Pythonista for
Github and is implemented on the Github API v3. This API requires a username and
password to login to a Github account.

When you have a Github account, follow these steps.

1. Execute gitter_search in Pythonista on your iOS device.
2. Enter the username at the prompt.
3. Enter the password at the prompt.

If everything was completed successfully you will then be prompted to choose the
type of search you want to do: 'user' or 'repo'. Just pressing return assumes the
default of 'user'.

The next prompt asks for a search query.

Github provides a mechanism to help specify a more complex query so that you can
find the users or repos that you might be interested in.

gitter_search has some built in short-cut queries that you can use. For user
searches you can enter `#poppy` (popular python), or for repo searches you can
enter `#poppy` (popular python) or `#poppista` (popular pythonista). In all
cases this uses the search query associated with the short-cut.

You are always able to manually enter your own queries. The query can be constrained
by using any of a number of qualifiers. They are as follows:

• `type:`  With this qualifier you can restrict the search to just personal accounts
(`user`) or organization accounts (`org`).
