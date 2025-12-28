m_dict={ 
    "what is result of 4+2:\n":"6",
    "what is freezing point of water (in C)?\n":"0",
    "what is the largest mammal on earth?\n":"whale",
    "what is the currency of japan?\n":"yen"
}
allkeys=list(m_dict.keys())
answer=None

def checkAnswer(qnumb,user_answer):
    if m_dict[allkeys[qnumb]]==answer:
        return True
    else:
        return False


print("**************quize game**************\n")
input("press enter to start the game ...")


for x in range(len(m_dict)):
    print(allkeys[x])
    answer=input()    
    print("answer is",checkAnswer(x,answer))

