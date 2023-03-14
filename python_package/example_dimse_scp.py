from pynetdicom import evt
import alpacs.dimse as dimse
from pprint import pprint

def handle_store(event):
        pprint(event)
        print("\nHANDLE THE STORED ITEM, AN EVENT {} HAS OCCURRED!!\n".format(event))
        return 0x0000
        
handlers = [(evt.EVT_C_STORE, handle_store)]

client_DIMSE = dimse.DimseClient("127.0.0.1", 201)
print("START SCP")
client_DIMSE.start_scp(handlers)

while True:
    key = input("Enter q to shudown\n")
    if (key == "q"):
          client_DIMSE.shutdown()
          break
