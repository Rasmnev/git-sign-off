# git-sign-off

This package serves to add and check git signatures to your repository.

This is useful when you want to add a certificate that certain command passed successfully
at a certain point of you repo timeline.

To automate such processes add a `git sign-off` command to your git pre-commit hooks, and on your CI check that they are up-to-date with a simple `git sign-off-check`.

# Installation

Just do it:
```bash
pip install git-sign-off
```

This installs two utilities `git-sign-off` and `git-sign-off-check` which you can use directly or through `git`'s command line.

# Usage


## Generate certificate

Let's say you want your developers to prove they executed a piece of code locally. Run this:

```bash
git sign-off -c bash <run_my_local_sensitive_test.sh>
```

If the "challenge" command executes successfully a certificate is added to your commit and you see this message:
> Added git-sign-off signature for task 'default'.


## Check certificate

```bash
git sign-off-check
```

If your certificate is not up-to-date you will have an error like:
>SignatureError: Outdated signature found. Latest signature was generated after commit:
>5c1537d3502b8bc17172b5a03a4531b010024754



