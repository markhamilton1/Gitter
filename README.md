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
by using any of a number of qualifiers. For a user search they are as follows:

• `type:`  With this qualifier you can restrict the search to just personal accounts
(`user`) or organization accounts (`org`). Example: `type:user`

• `in:`  Qualifies which name fields are searched. You can restrict the search to the
username field (`login`), the email field (`email`), or the real name field (`fullname`).
Example: `roger in:login` or `peter in:fullname`

• `repos:`  Filter users based on the number of repositories they have. Example: 
`repos:>10` or `repos:0..100`

• `location:`  Filter users based on the location indicated in their profile. Example:
`location:spain` or `location:usa`

• `language:`  Filter users based on the language used for one or more of their repos.
Example: `language:python`

• `created:`  Filter users based on when they created their Github account. Example:
`created:>=2015-01-25`

• `followers:`  Filter users based on the numbe of followers they have. Example:
`followers:>100`

For a repo search they are as follows:

• `created:`  Filter repos based on date of creation. Example: `created:>2015-01-25`

• `pushed:`  Filter repos based on date of last update. Example: `pushed:>=2015-01-20`

• `fork:`  Filter repos based only if they are forked (`only`) or include forked (`true`).
Example: `fork:only` or `fork:true`

• `forks:`  Filter repos based on the number of forks. Example: `forks:>=10`

• `in:`  Qualifies which name fields are searched. You can restrict the search to the name
field (`name`), description field (`description`), or readme field (`readme`).
Example: `astro in:name` or `astro in:description`

• `language:`  Filter repos based on the language they are written in.
Example: `language:python`

• `repo:`  Limit searches to specific repo.

• `user:`  Limit searches to specific user. Example: `user:mark`

• `size:`  Filter repos based on their size (in kilobytes). Example: `size:>=10` or
`size:<=100`

• `stars:`  Filter repos based on number of watchers. Example: `stars:>5`

• `topic:`  Filter repos based on the specified topic. Example: `topic:github` or
`topic:pythonista topic:dropbox`

In either case, multiple qualifiers may be specified by seperating them with spaces.
