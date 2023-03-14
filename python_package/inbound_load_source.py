import os

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

path = '/home/iagarcia/HippocampalMRISlices/01/'
dir_list = os.listdir(path)
Q = 9
channel_files, rest = split_list(dir_list, Q-1)

import threading
import time
import alpacs.dimse as dimse
from pprint import pprint
from pynetdicom.sop_class import MRImageStorage

def send_files(filenames, path):
    client_DIMSE = dimse.DimseClient("52.54.19.165", 100, "ALPACS")
    client_DIMSE.start_scu(MRImageStorage, "1.2.840.10008.1.2")
    for file in filenames:
        client_DIMSE.send_file(path+file)
    client_DIMSE.release()

threads = []
for i in range(Q-1):
    threads.append(threading.Thread(
        target=send_files,
        args=(channel_files[i],
        path)
    ))
threads.append(threading.Thread(target=send_files, args=(rest, path)))

start = time.time()
for i in range(Q):
    threads[i].start()
for i in range(Q):
    threads[i].join()
end = time.time()
print("ELAPSED TIME: {}".format(end-start))
