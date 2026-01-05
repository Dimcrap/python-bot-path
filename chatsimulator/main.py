
messges=["welcome to this  environments","how can i help you"]

class Chatbot:
   
   def __init__(self):
    self.state="start"

    

   options="/help\t/cancel\t/start\n/calculate" 
   help="this is a testing chatbot \nthere will be options available:\n"+options

   @staticmethod
   def calc():
        numb=input("enter a number")
        print(numb*0.50)
        print("\n",help)
      
   def handle_message(self,msg):
    if self.state=="start":
        if msg=="/start":
            #Chatbot.calc()
            print("welome !you are already in process \noption:",self.options)
        if msg=="/help":
            return help
        if msg=="/cancel":
            self.state="stop"
        if msg=="calculate":
           Chatbot.calc()
        else:
           print("unavalid input") 
    else:
       print("the bot is stoppeted!")


input("press enter to start ...")
bot=Chatbot()
while True:
   usrInput=input(bot.help+'\n')
   if usrInput=="/cancel":
      bot.handle_message(usrInput)
      break
   else:
      bot.handle_message(usrInput)
       
