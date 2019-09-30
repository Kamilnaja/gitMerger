import subprocess
initialBranch = "pex"
branchToCheckout = "0000"
ok = 'Already up to date'
cannotPull = 'cannot pull with rebase: You have unstaged changes'

def utf8Decode(input):
  return input.decode('utf-8')

try:
    output = subprocess.check_output(["git", "pull", "--rebase"])
except subprocess.CalledProcessError as e:
  print(e.output)
  pull = subprocess.check_output(["git", "stash"])
  print("stashing changes")
  # if cannotPull in utf8Decode(e.output):

# if ok in utf8Decode(output):
#   print(ok)
#   co = subprocess.check_output(["git", branchToCheckout])

# elif cannotPull in utf8Decode(output):
#   print('Need stash or commit')
# else:
#   print(utf8Decode(output))
