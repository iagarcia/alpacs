from pynetdicom import evt
import alpacs.dimse as dimse
from pprint import pprint

from dicomweb_client.api import DICOMwebClient
from dicomweb_client.session_utils import create_session_from_user_pass

session = create_session_from_user_pass(
        username='alpacs',
        password='4lp4cs!'
)

client = DICOMwebClient(
        url="http://127.0.0.1/dicom-web",
        session=session
)

def handle_store(event):
        pprint(event)
        ds = event.dataset
        client.store_instances(datasets=[ds])
        return 0x0000
        
handlers = [(evt.EVT_C_STORE, handle_store)]

client_1_DIMSE = dimse.DimseClient("127.0.0.1", 201, "ALPACS")
client_1_DIMSE.start_scp(handlers)

client_2_DIMSE = dimse.DimseClient("127.0.0.1", 202, "ALPACS")
client_2_DIMSE.start_scp(handlers)

client_3_DIMSE = dimse.DimseClient("127.0.0.1", 203, "ALPACS")
client_3_DIMSE.start_scp(handlers)

client_4_DIMSE = dimse.DimseClient("127.0.0.1", 204, "ALPACS")
client_4_DIMSE.start_scp(handlers)

client_5_DIMSE = dimse.DimseClient("127.0.0.1", 205, "ALPACS")
client_5_DIMSE.start_scp(handlers)

client_6_DIMSE = dimse.DimseClient("127.0.0.1", 206, "ALPACS")
client_6_DIMSE.start_scp(handlers)

client_7_DIMSE = dimse.DimseClient("127.0.0.1", 207, "ALPACS")
client_7_DIMSE.start_scp(handlers)

client_8_DIMSE = dimse.DimseClient("127.0.0.1", 208, "ALPACS")
client_8_DIMSE.start_scp(handlers)

client_9_DIMSE = dimse.DimseClient("127.0.0.1", 209, "ALPACS")
client_9_DIMSE.start_scp(handlers)
while True:
    key = input("Enter q to shudown\n")
    if (key == "q"):
          client_1_DIMSE.shutdown()
          client_2_DIMSE.shutdown()
          client_3_DIMSE.shutdown()
          client_4_DIMSE.shutdown()
          client_5_DIMSE.shutdown()
          client_6_DIMSE.shutdown()
          client_7_DIMSE.shutdown()
          client_8_DIMSE.shutdown()
          client_9_DIMSE.shutdown()
          break
