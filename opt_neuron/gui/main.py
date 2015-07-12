# coding: utf8

import logging
from .. import util
from gi.repository import Gtk
from threading import Thread

logger = logging.getLogger(__name__)
__out_queue = None
__in_queue = None
__msg = None

def main(in_queue, out_queue):
    global __out_queue 
    global __in_queue 
    global __msg
    global __running
    
    __out_queue = out_queue
    __in_queue = in_queue

    testWin = test(__in_queue, __out_queue)
    Gtk.main()
    
    receiver_t = Thread( target=receive )
    receiver_t.start()

def send_msg(*msg):
    for i in msg:
        logger.debug("Sent message: {msg}".format(msg=str(msg)))
        __out_queue.put(i)    
    
def __on_destroy():
    print("closing Gui!")
    __running = False
    Thread( target=self.sendit, args=(util.MESSAGE_EXIT,) ).start()
    Gtk.main_quit()
    print("asd")

def receive():
    global __msg
    __msg_read = 0
    while not __msg_read:
        __msg = __in_queue.get()
        if __msg is not None:
            #print(__msg)
            __msg_read = 1
    __msg_read = 0
            #alert = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, msg)
            #alert.connect("delete-event", alert.destroy)
            #alert.run()
            #print("msg box closed")
            #alert.destroy()
        

# returns __msg, which is containing the msg after using receive()     
def get_msg():
    global __msg
    receive()
    return __msg
    
from . import addframe
from . import mainframe
from . import sshframe


def test(in_queue, out_queue):   
    mf = mainframe.MainFrame(in_queue, out_queue) #MainFrame(root)
    mf.connect("delete-event", Gtk.main_quit)
    mf.show_all()

    #af = addframe.AddFrame()
    #af.connect("delete-event", Gtk.main_quit)      Das zerstört nur die komplette GUI, wenn das x genutzt wird!
    #af.show_all()
    
    #sf = sshframe.SshFrame(mf)
    #sf.connect("delete-event", Gtk.main_quit)      Das zerstört nur die komplette GUI, wenn das x genutzt wird!
    #sf.show_all()

