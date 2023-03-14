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
path = '/home/iagarcia/HippocampalMRISlices/01/'
dir_list = os.listdir(path)

# Channels
Q = 276
channel_files, rest = split_list(dir_list, Q)


from dicomweb_client.api import DICOMwebClient
from dicomweb_client.session_utils import create_session_from_user_pass
import pydicom

def send_files_dicomweb(filenames, path, i):
    session = create_session_from_user_pass(
        username='alpacs',
        password='4lp4cs!'
    )

    client = DICOMwebClient(
        url="http://18.232.238.142/dicom-web",
        session=session
    )
    for file in filenames:
        print("STOW-RS | Channel {} | {}".format(i, file))
        ds = pydicom.dcmread(path+file)
        client.store_instances(datasets=[ds])

# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
# creating thread

threads = []
for i in range(Q):
    threads.append(threading.Thread(target=send_files_dicomweb, args=(channel_files[i], path, i)))

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