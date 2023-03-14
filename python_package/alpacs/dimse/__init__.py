from pynetdicom import AE, debug_logger, evt
from pynetdicom import AllStoragePresentationContexts, ALL_TRANSFER_SYNTAXES

debug_logger()

class DimseClient:
    def __init__(self, ip, port, aet=""):
        self.ip = ip
        self.port = port
        self.aet = aet
        return
    
    def start_scp(self, handlers):
        ae = AE()
        storage_sop_classes = [
            cx.abstract_syntax for cx in AllStoragePresentationContexts
        ]
        for uid in storage_sop_classes:
            ae.add_supported_context(uid, ALL_TRANSFER_SYNTAXES)
        scp = ae.start_server((self.ip, self.port), block=False, evt_handlers=handlers)
        self.scp = scp
        return
    
    def shutdown(self):
        self.scp.shutdown()
        return
    
    def start_scu(self, uid, transfer_syntax):
        ae = AE()
        ae.add_requested_context(uid, transfer_syntax)
        assoc = ae.associate(self.ip, self.port, ae_title=self.aet)
        self.assoc = assoc
        return
    
    def send_file(self, filepath):
        if self.assoc.is_established:
            print('Association established with Store SCP!')
            self.assoc.send_c_store(filepath)
        else:
            print('Failed to associate')
        return

    def release(self):
        if self.assoc.is_established:
            self.assoc.release()
        else:
            print('Failed to release')
        return