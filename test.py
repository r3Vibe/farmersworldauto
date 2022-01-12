import json


def addclick(name,val):
    with open('click.json', 'r') as openfile:
        json_object = json.load(openfile)

    json_object[name] = val

    with open('click.json', 'w') as openfile:
        json.dump(json_object,openfile)



addclick('seed4',0)