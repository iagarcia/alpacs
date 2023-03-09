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

def send_files(assoc, filenames, path):
    for file in filenames:
        if (assoc.is_established):
            assoc.send_c_store(path+file)
        else:
            print('Association rejected, aborted or never connected', assoc)

# import OS module
import os
# Get the list of all files and directories
path = '/home/iagarcia/HippocampalMRISlices/01/'
dir_list = os.listdir(path)

# Channels
Q = 9
channel_files, rest = split_list(dir_list, Q)
print(rest)

from pydicom.dataset import Dataset

from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import MRImageStorage

debug_logger()

# Initialise the Application Entity
ae = AE()

# Add a requested presentation context
ae.add_requested_context(MRImageStorage)

# Associate with peer AE at IP 127.0.0.1 and port 11112
## assoc1 = ae.associate("52.54.19.165", 100, ae_title='ALPACS')

assoc0 = ae.associate("52.54.19.165", 100, ae_title='ALPACS')
assoc1 = ae.associate("52.54.19.165", 100, ae_title='ALPACS')
assoc2 = ae.associate("52.54.19.165", 100, ae_title='ALPACS')
assoc3 = ae.associate("52.54.19.165", 100, ae_title='ALPACS')
assoc4 = ae.associate("52.54.19.165", 100, ae_title='ALPACS')
assoc5 = ae.associate("52.54.19.165", 100, ae_title='ALPACS')
assoc6 = ae.associate("52.54.19.165", 100, ae_title='ALPACS')
assoc7 = ae.associate("52.54.19.165", 100, ae_title='ALPACS')
assoc8 = ae.associate("52.54.19.165", 100, ae_title='ALPACS')

# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
# creating thread
q0 = threading.Thread(target=send_files, args=(assoc0, channel_files[0], path,))
q1 = threading.Thread(target=send_files, args=(assoc1, channel_files[1], path,))
q2 = threading.Thread(target=send_files, args=(assoc2, channel_files[2], path,))
q3 = threading.Thread(target=send_files, args=(assoc3, channel_files[3], path,))
q4 = threading.Thread(target=send_files, args=(assoc4, channel_files[4], path,))
q5 = threading.Thread(target=send_files, args=(assoc5, channel_files[5], path,))
q6 = threading.Thread(target=send_files, args=(assoc6, channel_files[6], path,))
q7 = threading.Thread(target=send_files, args=(assoc7, channel_files[7], path,))
q8 = threading.Thread(target=send_files, args=(assoc8, channel_files[8], path,))

q0.start()
q1.start()
q2.start()
q3.start()
q4.start()
q5.start()
q6.start()
q7.start()
q8.start()

q0.join()
q1.join()
q2.join()
q3.join()
q4.join()
q5.join()
q6.join()
q7.join()
q8.join()

assoc0.release()
assoc1.release()
assoc2.release()
assoc3.release()
assoc4.release()
assoc5.release()
assoc6.release()
assoc7.release()
assoc8.release()