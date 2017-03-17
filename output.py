import sys
import re

with open(sys.argv[1]) as stats:
    lines = stats.readlines()
    bmisses = int(lines[5].strip().split(' ')[0].replace(',', ''))
    berr = float(re.sub(r".*\+\-  ([0-9.]*)% \).*", r"\1", lines[5]))
    cmisses = int(lines[8].strip().split(' ')[0].replace(',', ''))
    cerr = float(re.sub(r".*\+\-  ([0-9.]*)% \).*", r"\1", lines[8]))
    llcmisses = int(lines[12].strip().split(' ')[0].replace(',', ''))
    llcerr = float(re.sub(r".*\+\-  ([0-9.]*)% \).*", r"\1", lines[12]))
    seconds = float(lines[14].strip().split(' ')[0])

score = (seconds*30 + cmisses/1e7 + bmisses/1e7 + llcmisses/1e6)/6

if score > 5000:
    score = 5000

print(score)
