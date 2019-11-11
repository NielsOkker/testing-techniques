import json
import subprocess

def dejsonfy(jsonArray):
    array = []
    for i in jsonArray:
        array.append(i['currentElementName'])
    return array

def handle_currentElement(ce):
    if ce == "v_Normal":
        print("Handle v_Normal")
    elif ce == "v_Insert":
        print("Handle v_Insert")
    elif ce == "e_Ctrl-C":
        print("Handle e_Ctrl")
    elif ce == "e_Esc":
        print("Handle e_Esc")
    else:
        print("Handle Insert command")


#Start
var = subprocess.check_output(['java', '-jar', 'graphwalker-cli-4.0.1.jar', 'offline', '-m', \
    'undefined.json', '"quick_random(edge_coverage(100))"'])

var = var.splitlines()
stateArray = []
for v in var:
    stateArray.append(json.loads(v)['currentElementName'])

for i in stateArray:
    handle_currentElement(i)