import subprocess
initialBranch = "pex"
branchToCheckout = "0000"
ok = 'Already up to date'
cannotPull = 'cannot pull with rebase: You have unstaged changes'


def utf8Decode(input):
    return input.decode('utf-8')


def checkout():
<<<<<<< HEAD
    print(ok)
    co = subprocess.check_output(["git", "checkout", branchToCheckout])
    status = subprocess.check_output(["git", "status"])
    print(status)
=======
    print('starting checkout')
    try:
      co = subprocess.check_output(["git", "checkout", branchToCheckout])
      status = subprocess.check_output(["git", "status"])
      print(status)
    except subprocess.CalledProcessError as e:
        print(e)

>>>>>>> 0000


def stash():
    stash = subprocess.check_output(["git", "stash"])
    print(stash)
    print("stashing changes success")


def amend():
    amend = subprocess.check_output(["git", "commit", "--amend", "--no-edit"])
    print(amend)
    print("amend successfull")


def askForAction():
    print("Do you want [s]tash or [a]mend your changes?")
    action = input()
    if action == "s":
        stash()
    elif action == "a":
        amend()

def doGitActions():
  try:
      output = subprocess.check_output(["git", "pull", "--rebase"])
      if ok in utf8Decode(output):
          checkout()
  except subprocess.CalledProcessError as e:
      print(e.output)
      askForAction()
<<<<<<< HEAD
=======
      checkout()
>>>>>>> 0000

doGitActions()