# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
char = input()
pattern = r"([a-zA-Z0-9])\1+"
match = re.search(pattern,char)
if match:
    print(match.group(1))
else:
    print(-1)
