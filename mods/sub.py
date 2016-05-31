#essential
import _thread as thread
from queue import *

#mod
import urllib.request

class sub:
    def __init__(self, bot):
        self.name="sub"
        self.bot = bot
        self.queue_in=Queue()
        #self.queue_out=Queue()
        thread.start_new_thread(self.run,())
        #self.resttime=0
        #self.lastcmd=0
        self.subwaylink="http://subdestag.es"

    def run(self):
        while 1: 
            msg=self.queue_in.get() # get() is blocking
            chat_id=msg.get_chat_id()
            if msg.get_text()=="/sub":
                content=urllib.request.urlopen(self.subwaylink).read().decode("utf-8").strip('\n\r')
                try:
                    sub=content.split("<h1>")[1].split("</h1>")[0]
                    ingr=content.split("<h4>")[1].split("</h4>")[0]
                    msg=sub # set it to sub only
                    if (sub!=ingr):
                        msg="%s (%s)"%(sub,ingr) # add the ingredients on deviation
                except IndexError:
                    msg="parser broken or page down..." # error
                self.bot.sendMessage(chat_id,msg)

    def enqueue(self,msg):
        self.queue_in.put(msg)