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