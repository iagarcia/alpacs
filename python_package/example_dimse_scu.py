import alpacs.dimse as dimse
from pprint import pprint
from pynetdicom.sop_class import CTImageStorage, MRImageStorage
from pydicom.uid import ExplicitVRLittleEndian, SecondaryCaptureImageStorage

client_DIMSE = dimse.DimseClient("127.0.0.1", 201)
print("START SCU")
client_DIMSE.start_scu(CTImageStorage,'1.2.840.10008.1.2.4.70')
client_DIMSE.send_file('sample2.dcm')
client_DIMSE.release()