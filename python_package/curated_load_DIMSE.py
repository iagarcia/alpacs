def split_list(dir_list, Q):
    K = len(dir_list)
    k = int(K/Q)
    channel_files = []
    rest = []

    if (K >= Q):        
        for q in range(Q):
            channel_files.append(dir_list[q*k:(q+1)*k])
        rest = dir_list[(1+q)*k:]
    else:
        for q in range(Q):
            if (K > q):
                channel_files.append([dir_list[q]])
            else:
                channel_files.append([])

    return channel_files, rest

# import OS module
import os
# Get the list of all files and directories
path = '/home/iagarcia/ALPACS/python_package/dcm_samples/'
dir_list = os.listdir(path)

# Channels
Q = 4
channel_files, rest = split_list(dir_list, Q)

from pydicom.dataset import Dataset
from pydicom.uid import ImplicitVRLittleEndian, JPEGBaseline
from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import MRImageStorage
from pynetdicom.sop_class import CTImageStorage
from pynetdicom import build_context
from pynetdicom.sop_class import Verification

debug_logger()

def send_files(filenames, path, i):
    ae = AE()
    ae.requested_contexts = [build_context(Verification, "1.2.840.10008.5.1.4.1.1.7")]
    ae.add_requested_context(MRImageStorage)   
    ae.add_requested_context(CTImageStorage, ImplicitVRLittleEndian)
    ae.add_requested_context(CTImageStorage, JPEGBaseline)
    assoc = ae.associate("18.232.238.142", 4242, ae_title='ALPACS')
    for file in filenames:
        print("STORE-C | Channel {} | FILE {}".format(i, file))
        if (assoc.is_established):
            assoc.send_c_store(path+file)
        else:
            print('Association rejected, aborted or never connected', assoc)
    assoc.release()

print(rest)

# Initialise the Application Entity
# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
# creating thread

threads = []
for i in range(Q):
    threads.append(threading.Thread(target=send_files, args=(channel_files[i], path, i)))

import time

start = time.time()

for i in range(Q):
    threads[i].start()

for i in range(Q):
    threads[i].join()

end = time.time()
print("ELAPSED TIME")
print(end - start)
dif = time.localtime(end-start)
print(dif)
