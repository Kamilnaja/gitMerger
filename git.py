ok = 'Already up to date'
cannotPull = 'cannot pull with rebase: You have unstaged changes'
import subprocess
output = subprocess.check_output(["git", "pull", "--rebase"])

def utf8Decode(input):
  return input.decode('utf-8')

if ok in utf8Decode(output):
  print(ok)
elif cannotPull in utf8Decode(output):
  print('Need stash or commit')
else:
  print(utf8Decode(output))