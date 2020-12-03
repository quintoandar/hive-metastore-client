# Hive Metastore Client's WorkFlow

## Features

A feature is based on the `main` branch and merged back into the `main` branch.

![](https://docs.microsoft.com/en-us/azure/devops/repos/git/media/branching-guidance/featurebranching.png?view=azure-devops)


### Working Locally

```
# checkout main, fetch the latest changes and pull them from remote into local
git checkout main
git fetch
git pull origin main

# create a feature branch that is based off main
git checkout -b <username>/some-description

# add your work
git add something
git commit -m "first commit"
git add another
git commit -m "second commit"

# rebase against main to pull in any changes that have been made
# since you started your feature branch.
git fetch
git rebase origin/main

# push your local changes up to the remote
git push

# if you've already pushed changes and have rebased, your history has changed
# so you will need to force the push (use this command wisely!)
git fetch
git rebase origin/main
git push --force-with-lease 
````


### GitHub workflow

- Open a Pull Request against `main`. Check our PR guidelines [here](https://github.com/quintoandar/hive-metastore-client/blob/main/CONTRIBUTING.md#pull-request-guideline).
- When the Pull Request has been approved, merge using `squash and merge`, adding a brief description:
i.e., `Add new parameter X in TableBuilder`.
- This squashes all your commits into a single clean commit. Remember to clean detailed descriptions, otherwise our git logs will be a mess.

If you are unable to squash merge because of conflicts, you need to rebase against `main` again:

```
# in your feature branch
git fetch
git rebase origin/main

# fix conflicts if they exist, add and commit them (git add & git commit)
git push --force-with-lease
```


## Releases

The release will always occur when we change the version in the setup.py file.


### Working Locally

```
# create a feature branch
git checkout main
git fetch
git pull origin main
git checkout -b release/<version>

# finalize the changelog, bump the version into setup.py and update the documentation then:
make update-docs
git add CHANGELOG.md
git add setup.py
git commit -m "release <version>"

# push the new version
git fetch
git push --force-with-lease
```

### Github workflow

- Open a Pull Request against `main`.
- When the PR's approved and the code is tested, `squash and merge` to squash your commits into a single commit.
- The creation of the release tag and the update of the PyPi version will be done 
automatically from the Publish workflow, you can follow [here](https://github.com/quintoandar/hive-metastore-client/actions?query=workflow%3APublish).

### Update API Documentation

If new information was added in the documentation in the release, maybe you will need to update our hosted Documentation. It's super simple, in the **docs** folder just apply the modifications and open a PR:

If you want to test your changes locally, just run:
 
```bash
make docs
```

And open `index.html` file. 

No need to worry about modifying the `API Documentation`,  everything is generated from [Sphinx](https://www.sphinx-doc.org/en/master/index.html) and hosted by [ReadtheDocs](https://readthedocs.org/). But your documentation changes will only be applied after a merge to main branch.


## Hotfixes

A hotfix is a patch that needs to go directly into `main` without going through the regular release process.
The most common use case is to patch a bug that's on production when `hotfix` contains code that isn't yet ready for release.

Another use case is when a past release needs a patch. For example, we are currently on version 3.2 but find a critical 
bug that is present since 2.5 and want to fix it. Then we would create a hotfix branch and release it as 2.5.1.

### Working locally

```
# create a hotfix branch based on main, because main is what will be deployed to production
git checkout main@<version>
git fetch
git pull origin main
git checkout -b hotfix/<version>
git checkout -b describe-the-problem

git add patch.fix
git add setup.py
git commit -m "fix the problem"
git push
```

Don't forget to update the Changelog and the version in `setup.py`.

### Github workflow

- Open a Pull Request against `hotfix/<version>`
- When the PR's approved and the code is tested, `squash and merge` to squash your commits into a single commit.
- A tag will automatically be triggered in our CI/CD. This tag/release will use the version for its title and push a new version
of Hive Metastore Client's python package to our private server.

You may always update the tag/release description with the changelog.
