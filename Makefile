.DEFAULT_GOAL := git-push

# Ref -> https://stackoverflow.com/a/26737258/667301
# Ref -> https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/
.PHONY: git-push
git-push:
	@echo ">> checkout master branch, push to origin/master, switch back to develop"
	ping -q -c1 -W1 4.2.2.2                   # quiet ping...
	-git checkout master || git checkout main # Add dash to ignore checkout fails
	THIS_BRANCH=$(shell git branch --show-current)  # ENV var assignment, no space
	git merge @{-1}                           # merge the previous branch...
	git push origin $(THIS_BRANCH)            # push to origin / $THIS_BRANCH
	git checkout @{-1}                        # checkout the previous branch...

