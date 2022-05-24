import re
import time

#definition to read the content of the file. the file should be in 
def read_file():
    with open("samplelog.txt", "r") as f:
        test = f.read()
    return test
#regex which will split the log lines till log Level
regex = re.compile(r'([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{1,3})?,[0-9]+\s\[[^\]]*\]\s(TRACE|DEBUG|INFO|NOTICE|WARN|WARNING|ERROR|SEVERE|FATAL))')
#initial stores the lines already contained in the file
initial = read_file()

while True:                                                     # will run perpetually, looking for new log lines addition in the file
    time.sleep(1)                                               # added to decrease the number of times the file is read per second
    current = read_file()
    if initial != current:                                      # checks if there is any new line added       
        newlogs = current.removeprefix(initial)                 # newlogs variable stores the newly added lines
        newlog = regex.split(newlogs)                           # newlog variable stores the logs splitted, in list format
        err=""
        for i in range(3,len(newlog),4):
            if (newlog[i] == 'ERROR' or newlog[i] == 'SEVERE' or newlog[i] == 'FATAL'):# all log lines greater that WARNING level gets stored and printed
                err = err + str(newlog[i-2])+str(newlog[i+1])
        print(err)
    initial = current