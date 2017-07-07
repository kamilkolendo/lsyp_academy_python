import requests
import json

base_url = "https://issues.apache.org/jira/rest/api/2/"
path = "issue/ZOOKEEPER-2613"

URL = "https://issues.apache.org/jira/rest/api/2/issue/ZOOKEEPER-2613"
r = requests.get(URL, verify=False)

json_dict = r.json() # a standard python dictionary
print(json.dumps(json_dict, indent=3)) # to pretty-print with 3 spaces of indentation

print(json_dict['key'])

#sprawdzanie czy jakis string zawiera sie w innym:
counter = 0
if "ZOOKEEPER" in URL:
    counter+=1