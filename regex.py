import re

message = "File saved at 17:23:57"

pattern = "\d\d:\d\d:\d\d" # \d is a digit

m = re.search(pattern, message)

if m: # would be None if no match is found
    print(m.group())

###

message = "My email is kol3ndo@gmail.com and I'm cool. abc@abc.pl"

pattern = "[a-z0-9.]+@[1-z.]+\.[a-z]{1,3}" # \d is a digit

m = re.findall(pattern, message)

if m: # would be None if no match is found
    print(m)