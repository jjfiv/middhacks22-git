# MiddHacks '22 Git Tutorial

A repository & bot that must have the last word makes for a decent git tutorial.

## Get Access!

Create a Github account and send it to the workshop organizer!

## First Time Git Setup

You may have already done this!

```bash
# Git writes your name and email on your contributions.
git config --global user.name "John Doe"
# Try to use the same email you used to sign up for github!
git config --global user.email johndoe@example.com
# switch from vim to nano / emacs / code / etc.
git config --global core.editor nano
```

## Clone & Create Your Own File:

This will set you up to work with 'best-case scenario git', where you're working on different files than other people.

See [Issue#1](https://github.com/jjfiv/middhacks22-git/issues/1) for some more detailed instructions.

1. Observe ``last-word-bot`` committing the time over you. (Every minute, it will check to see and make sure it's the last modification!)
2. Practice editing the file and dealing with the need to pull and push to get your changes into ``main``.

## Merge Conflict Practice

1. Find a partner.
2. Choose one of your files to work on.
3. Both edit the same file (one add a comment at top, one add at the bottom.)
4. Choose one of you to win.
5. commit, (push/pull)+
6. Go back and let the other one try. See that Git can resolve some changes automatically!
7. Now go back, and both try again, editing the same lines. See how it gives up and gives you all the information it can into the file? Choose a winner, delete all the "ascii art <<<< ==== >>>>" and commit, (push/pull)+.

## How does it work?

``last-word-bot/update.sh`` is a script in python/bash that pulls from the git repository and submits a ``last-word-bot/timestamp`` update if it has changed. It has infinite patience and will get the last word.
