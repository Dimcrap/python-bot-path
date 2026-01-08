import random
import datetime

class mockAPI:
    messages_queue=[]
    bots_replies=[]
    
    def add_to_queue(msg):
        mockAPI.messages_queue.append(msg)

    def get_updates():
        if mockAPI.messages_queue:
            return mockAPI.messages_queue
        else:
            return -1

    def sendMessage(self,chatId,textmsg):
        responde={"chat_id":chatId,"message":textmsg}
        self.bots_replies.append(responde)

    def process_bot_response():



'''
    def handle_message(self,usr_id,text):
        #pend the massage and put them in queue'''

class Chatbot:
   options="/help\t/cancel\t/start\n/calculate" 
   help="this is a testing chatbot \nthere will be options available:\n"+options
   
  def __init__(self):
        self.state="start"
    
    
  def handle_message(self,msg):
    #analyze and process the msg and then use mockAPI.send_message()
    """if self.state=="start":
        if msg=="/start":
            #Chatbot.calc()
            print("welome !you are already in process \noption:",self.options)
        elif msg=="/help":
            print( self.help)
        elif msg=="/cancel":
            self.state="stop"
        elif msg=="/calculate":
           Chatbot.calc()
        else:
           print("unavalid input") 
    else:
       print("the bot is stoppeted!") """

class clientInterface:
        
    def __init__(self,api_instance):
        self.api=api_instance

    def create_message(id,txt):
        return {
        "message_id": random.randint(1,100000),
        "from": {"id": id},
        "chat": {"id": 456},
        "text": txt ,#"/start",
        "date": datetime.datetime.now()
        }
        
    def client_sendmsg(self,usr_id,text,mockAPI.):
        message=clientInterface.create_message(usr_id,text)
        self.api.add_to_queue(message)


interface=clientInterface()
while 