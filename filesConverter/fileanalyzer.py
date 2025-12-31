class analyzer:
    def countWord(filePath):
        count=0
        with open(filePath) as file:
            data=file.read()
            lines=data.split()
            for word in lines:
                if not is_num(word):
                    count+=1
        return count
            
    def countNumbs(filePath):
        count=0
        with open(filePath) as file:
            data=file.read()
            lines=data.split()
            for word in lines:
                if is_num(word):
                    count+=1
        return count
    def test():
        print("analayzer class connected")
    
    def uniqueWcount(filePath):
        with open(filePath,"r") as file:
            filedata=file.read()
            Uwords=set(filedata.split())
            return len(Uwords)
def is_num(input):
    try:
        float(input)
        return True
    except ValueError:
        return False
    
def extractName(path):
    nameS=path.find("/f")
    nameE=path.find(".txt")
    name=""
    for i in range(nameS+1,nameE):
        name=name+path[i]
    return name

def makeDict(path):
    return {"filename":extractName(path),"wordsCount":analyzer.countWord(path),
            "numberscount":analyzer.countNumbs(path),"uniquewords":analyzer.uniqueWcount(path)}

def make_dictlist(pathlist):
    list=[]
    for path in pathlist:
        #print("path for ")
        m_dict=makeDict(path)
        list.append(m_dict)
    return list
