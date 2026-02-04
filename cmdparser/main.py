
deposits=[]
raks=[{"number":"001","status":"filled"},{"number":"002","status":"not-filled"},
       {"number":"003","status":"filled"},{"number":"004","status":"not-filled"}]

#testcases: "/start","/stop","/time",
# "/status_rak -number-",
# "/deposit -name- -amount-",
# /find_empty_rak -[number]=default=>1-  

class commandParser:

    def __init__(self,depList,rakList):
        self.deposits=depList
        self.raks=rakList

    def parser(self,input):
        command={"command":"","countflag":"","values":{}}
        if input.find("find_empty_rak"):
            if input[17]=="-":
                details=(input[18:input.len()]).split()
                command["command"]="find_rak"
                command["countflag"]=details[0]                
                self.router(command)
            else:
                self.router("find")
        if input.find("deposit"):
            fullStr=raks.split()
            self.router("deposit",{"name":fullStr[1],"amount":fullStr[2]})
        if input.find()    
            


    def router(slef,command,dict):

    def is_validate();    

