import random
import datetime

class mockAPI:
    messages_queue=[]
    bots_replies=[]
    
    def add_to_queue(msg):
        mockAPI.messages_queue.append(msg)

    def get_updates():
        if mockAPI.messages_queue:
            return mockAPI.messages_queue[0]
        else:
            return -1

    def sendMessage(self,chatId,textmsg):
        responde={"chat_id":chatId,"message":textmsg}
        self.bots_replies.append(responde)

    def invoke_bot_response():
        
       

class Chatbot:
   
   def __init__(self,api_instance):
        self.api=api_instance
   #     self.state="start"
    
   options="/help\t/cancel\t/start\n/calculate" 
   help="this is a testing chatbot \nthere will be options available:\n"+options
   advices=["Set goals — Don’t expect to achieve anything if you don’"
            "t know what your end goal is supposed to be. Set destination, then set sail.",
            "Celebrate all the successes — no matter how small, a win is a win, especially "
            "when we take losses harder than we should. Take advantage of it.",
            "Make decisions based on data if you can — Numbers don’t lie",
            "Trust your gut — Data-based decisions are only helpful if you have data,"
             " if not, always trust your gut.",
            "Follow the 80/20 rule — 20% of your work will bring 80% of your results."
             " Find that 20% work and focus on that.",
             "Do what you love — life is really short, if you don’t love the work you’re"
              " doing or isn’t leading to the work that you‘ll enjoy, then it’s not worth doing.",
            "Take initiative — I’ve had problems with this and that’s making an impact without being "
            "told what to do. This separates successful from the mediocre"
            ]

   def insertReply(self,replytxt):
       self.api.bots_replies.append(replytxt)
       
        
   def handle_message(self):
        reply=""
        msg=self.api.get_updates()
        txt=msg["text"]
        usr=msg["from"]
        msgID= msg["message_id"]
        chatID=msg["chat"]

        if txt=="/start":
            reply="welome !you are already in process \noption:"+self.options
        elif txt=="/help":
            reply=self.help
        elif txt=="/cancel":
            self.state="stop"
            reply="bot stopped"
        elif txt=="/advice":
           reply=Chatbot.advices[random.randint(0,6)]
        else:
           reply="unavalid input"
        Chatbot.insertReply({"method":"sendMessage","user_id":usr["id"],
                             "message_id":msgID,"chat_id":chatID["id"],"text":reply})



class clientInterface:
        
    def __init__(self,api_instance):
        self.api=api_instance
        self.userId=random.randint(1,100)

    def create_message(self,txt):
        return {
        "message_id": random.randint(1,100000),
        "from": {"id": self.userId},
        "chat": {"id": 456},
        "text": txt ,#"/start",
        "date": datetime.datetime.now()
        }
        
    def client_sendmsg(self,text,mockAPI):
        message=clientInterface.create_message(text)
        self.api.add_to_queue(message)

telegramapi=mockAPI()
bot=Chatbot()
interface=clientInterface(telegramapi)
while 