.DEFAULT_GOAL := git-push

# Ref -> https://stackoverflow.com/a/26737258/667301
# Ref -> https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/
.PHONY: git-push
git-push:
	@echo ">> checkout master branch, push to origin/master, switch back to develop"
	ping -q -c1 -W1 4.2.2.2                   # quiet ping...
	-git checkout master || git checkout main # Add dash to ignore checkout fails
	# Use perl for env variable assignment... Makefile needs double-dollar escapes
	perl -e '$$ENV{"THIS_BRANCH"}=`git branch --show-current`;'
	git merge @{-1}                           # merge the previous branch...
	git push origin $(THIS_BRANCH)            # push to origin...
	git checkout @{-1}                        # checkout the previous branch...

