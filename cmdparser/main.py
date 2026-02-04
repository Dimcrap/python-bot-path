import datetime
import ast

deposits=[]
raks=[{"number":"001","status":"filled"},{"number":"002","status":"not-filled"},
       {"number":"003","status":"filled"},{"number":"004","status":"not-filled"},
       {"number":"005","status":"not-filled"},{"number":"006","status":"not-filled"}]


class commandParser:

    def __init__(self,depList,rakList):
        self.deposits=depList
        self.raks=rakList

    def parser(self,input):
        command={"command":"","countflag":"","values":{}}
        fullStr=input.split()

        if input.find("find_empty_rak")!=-1:
            if len(input)>15:
                details=(input[17:len(input)]).split()
                command["command"]="find_rak"
                command["countflag"]=details[0]                
            else:
                command["command"]="find_rak"
                command["countflag"]="1"
        elif input.find("deposit")!=-1:
            command["command"]="deposit"
            command["values"]={"name":fullStr[1],"amount":fullStr[2]}
        elif input.find("status_rak")!=-1:
                command["command"]="status"
                command["values"]={"number":fullStr[1]}
        elif not input.find("start") or not input.find("stop") or not input.find("time"):
            command["command"]="error"
        else:
            command["command"]=fullStr[0]
        self.router(command)

    def router(self,commandDict):
        if(commandDict["command"])=="find_rak":
            self.rakfinder(commandDict["countflag"])
        elif commandDict["command"]=="deposit":
            self.depositor(commandDict["values"]) 
        elif commandDict["command"]=="status":
            self.rakreport(commandDict["values"]["number"])
        elif commandDict["command"]=="error":
            print("unvalid input detected!\nprocess failed")
        else:
            self.headfunc(commandDict["command"]) 
                               
    def rakfinder(self,instruct):    
        raks_namelist=[]
        start=0
        for x in range(int(instruct)):
                for index in range(start,len(self.raks)):
                    if (self.raks[index]["status"]=="not-filled"):
                        raks_namelist.append(self.raks[index]["number"])
                        start=index+1
                        break

        print(raks_namelist)         

    def depositor(self,instruct):        
        self.deposits.append(instruct)
         
    def rakreport(self,raknumber):
         status=""
         for rak in self.raks:
                if rak["number"]==raknumber:
                    status=rak["status"]
         print(f"rak number {raknumber} is {status}")

    def headfunc(self,cmd):
         if cmd=="/start":
              print("welcome to the process -guides . . .")
         elif cmd=="/stop":
              print("process stopped=>reuse it with starting it")
         elif cmd=="/time":
              print(datetime.datetime.now())
         else:
              print("unvalid command recieved\nprocess failed")     

#testcases: "/start","/stop","/time",
# "/status_rak -number-",
# "/deposit -name- -amount-",
# /find_empty_rak -[number]=default=>1-  

cmdparser=commandParser(deposits,raks)

#cmdparser.parser("/start")
#cmdparser.parser("/stop")
#cmdparser.parser("/time")

#cmdparser.parser("/status_rak 004")

#cmdparser.parser("deposit ahlam 2355")
#print(deposits)

cmdparser.parser("/find_empty_rak -4")

