import re
from zipfile import ZipFile

with ZipFile("access_log_Jul95.zip") as zipper:
    zipper.extractall()

logFile = open("access_log_Jul95", "r")
text = logFile.read()
allRequest = re.findall(
    "(\[07/Jul/1995:(10:59:(2[8,9]|[3-5][0-9])|(1[1,9]|2\d):\d\d:\d\d)| \[08/Jul/1995:((0\d|1[0-8]):\d\d:\d\d|19:([0-2]\d:\d\d|3([0-4]:\d\d|5:(0\d|1[0,1]))))).+\"HEAD.+HTTP/\d\.\d\"\s200",
    text)
print(len(allRequest))
print("-------------------------")
allRequest.clear()

logFile = open("access_log_Jul95", "r")
allLines = logFile.readlines()
for line in allLines:
    if re.search(
            '(\[07/Jul/1995:(10:59:(2[8,9]|[3-5][0-9])|(1[1,9]|2\d):\d\d:\d\d)| \[08/Jul/1995:((0\d|1[0-8]):\d\d:\d\d|19:([0-2]\d:\d\d|3([0-4]:\d\d|5:(0\d|1[0,1]))))).+\"HEAD.+HTTP/\d\.\d\"\s200',
            line):
        allRequest.append(line)

for req in allRequest:
    print(req)
