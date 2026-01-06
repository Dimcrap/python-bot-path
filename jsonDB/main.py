import json


def usridGenerator():
    with open("database.json",'r+') as db:
        data=json.load(db)

    lastId=data['lastIDs']['lastUsr']
    #print(lastId)
    data['lastIDs']['lastUsr']=lastId+1
    with open("database.json",'w') as writedb:
        json.dump(data,writedb)
    return str(lastId+1)

def getUsrInfo():
    user={"name":"","chatStatus":"","language":"","createDate":"","prefrences":{}}
    user["name"]=input("enter username")
    print("username is ",user["name"])

def insertuser(usrDict):
    usrId=usridGenerator()
    usr="1"
    

    with open("database.json","r") as rfile:
        data=json.load(rfile)
    if usr not in data["users"]:
        data["users"][usr]={}
    data["users"][usr]["name"]="valuename"
    

    with open("database.json",'w') as rfile:
        json.dump(data,rfile,indent=2)

#insertuser()
getUsrInfo()

    
