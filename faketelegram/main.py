import random
import threading
import datetime
import time


class mockAPI:
    messages_queue=[]
    bots_replies=[]
    
    def add_to_queue(self,msg):
        self.messages_queue.append(msg)

    def get_updates(self):
        if self.messages_queue:
            message=self.messages_queue[0]
            del self.messages_queue[0]
            return message
        else:
            return -1

    def get_rep_updates(self,ID):
        if self.bots_replies:
           indx=0
           for rep in self.bots_replies:
                if(rep["user_id"]==ID):
                    reply=rep
                    
           indx=self.bots_replies.index(reply)
           del self.bots_replies[indx]
           return reply
        else:
            return -1    
        
       
class Chatbot:
   
    def __init__(self,api_instance):
        self.api=api_instance
    #     self.state="start"
        self.thread=threading.Thread(target=self._check_loop,daemon=True)
    
    options="/help\t/cancel\t/start\n/advice" 
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

    def start(self):
        self.thread.start()
    
    def _check_loop(self):
       while True:
           message=self.api.get_updates()
           if not message==-1:
               self.handle_message(message)
               
           time.sleep(0.1)
               
    def insertReply(self,replytxt):
       self.api.bots_replies.append(replytxt)
           
    def handle_message(self,msg):
        reply=""
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
        self.insertReply({"method":"sendMessage","user_id":usr["id"],
                             "message_id":msgID,"chat_id":chatID["id"],"text":reply})


class clientInterface:
        
    def __init__(self,api_instance):
        self.api=api_instance
        self.userId=random.randint(1,100)
        self.thread=threading.Thread(target=self._check_loop,daemon=True)


    def showReply(self,botReply):
        print(botReply["text"])

    def _check_loop(self):
        while True:
            reply=self.api.get_rep_updates(self.userId)
            if reply!=-1:
                self.showReply(reply)
            time.sleep(0.1)

    def start(self):
        self.thread.start()

    def create_message(self,txt):
        return {
        "message_id": random.randint(1,100000),
        "from": {"id": self.userId},
        "chat": {"id": 456},
        "text": txt ,
        "date": datetime.datetime.now()
        }
        
    def client_sendmsg(self,text):
        message=self.create_message(text)
        self.api.add_to_queue(message)


telegramapi=mockAPI()
bot=Chatbot(telegramapi)
interface=clientInterface(telegramapi)
bot.start()
interface.start()



#interface.client_sendmsg("/start")
interface.client_sendmsg("/advice")
time.sleep(3)
#print(telegramapi.messages_queue)

