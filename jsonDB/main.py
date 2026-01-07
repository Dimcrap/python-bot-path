import json
import datetime

def usridGenerator():
    with open("database.json",'r+') as db:
        data=json.load(db)

    lastId=data['lastIDs']['lastUsr']
    #print(lastId)
    data['lastIDs']['lastUsr']=lastId+1
    with open("database.json",'w') as writedb:
        json.dump(data,writedb)
    return str(lastId+1)

def checkConds(statement1,statement2,value):
    if value==statement1:
        return True
    elif value==statement2:
        return True
    else:
        return False

def getUsrInfo():
    user={"name":"","chatStatus":"","language":"","createDate":"","prefrences":{"getnews":"","getGroupsLink":""}}
    user["createDate"]=datetime.datetime.now()
    #print("created time ",user["createDate"])
    user["name"]=input("enter username:")
    stInput=input("chat status (1-authenticated 2-waiting for authentication):")
    while  not stInput.isnumeric() or 0>int(stInput) or int(stInput)>2:
        stInput=input("unvalid input!\nchat status (1-authenticated 2-waiting for authentication):")
    user["chatStatus"]="Authenticated" if stInput=="1" else "waiting_for_authentication"        
    
    nameInput=input("choose language en(english)/per(persian):")
    while checkConds("en","per",nameInput)==False:
        nameInput=input("Unvalid input!\nchoose language en(english)/per(persian):")    
    user["language"]=nameInput

    preInput=input(" getting news (on/off):")
    while checkConds("on","off",preInput)==False:
        preInput=input("Unvalid input!\n getting news (on/off):")
    user["prefrences"]["getnews"]=preInput
    
    preInput=input(" getting groups invite links (on/off):")
    while checkConds("on","off",preInput)==False:
        preInput=input("Unvalid input!\n getting getting groups invite links (on/off):")
    user["prefrences"]["getGroupsLink"]=preInput

    return user

def insertuser(usrDict):
    usrId=usridGenerator()
    
    with open("database.json","r") as rfile:
        data=json.load(rfile)
    if usrId not in data["users"]:
        data["users"][usrId]={}
    if "prefrences" not in data["users"][usrId]:
        data["users"][usrId]["prefrences"]={}
    
    data["users"][usrId]["name"]=usrDict["name"]
    data["users"][usrId]["chatStaus"]=usrDict["chatStatus"]
    data["users"][usrId]["language"]=usrDict["language"]
    data["users"][usrId]["createDate"]=str(usrDict["createDate"])
    data["users"][usrId]["prefrences"]["getnews"]=usrDict["prefrences"]["getnews"]
    data["users"][usrId]["prefrences"]["getGtoupLinks"]=usrDict["prefrences"]["getGroupsLink"]
    print("before writing",data)

    with open("database.json",'w') as rfile:
        json.dump(data,rfile)


newuser=getUsrInfo()
insertuser(newuser)

    
