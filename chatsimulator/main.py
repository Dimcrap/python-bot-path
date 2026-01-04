
messges=["welcome to this  environments","how can i help you"]

class Chatbot:
   def __int__(self):
    self.state="start"
   
   help="this is a testing chatbot \nthere will be options available:\n/help\t/cancel\n/start"

   @staticmethod
   def mainfunction():
        numb=input("enter a number")
        print(numb%2)
      
   def handle_message(self,msg):
    if self.state=="start":
        if msg=="/start":
            Chatbot.mainfunction()
        if msg=="/help":
            return help
        if msg=="/cancel":
            self.state="stop"
        
