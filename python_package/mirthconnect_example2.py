import  alpacs.mirthconnect as mc
from pprint import pprint

client_MC = mc.MirthConnectClient(
    "52.54.19.165",
    "8443",
    "alpacs",
    "4lp4cs!",
    "keystore.jks",
    "mirthpass"
    )
client_MC.start_connection()
channels = client_MC.get_channels()

print(channels)

channel_id = "f32dc40f-2aeb-49b7-8ebd-2100d40dff53"
response = client_MC.delete_channel(channel_id)