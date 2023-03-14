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

pprint(vars(client_MC))

users = client_MC.get_users()

pprint(users)

client_MC.post_inbound_channel('inbound_channel.xml', 'inbound_channel_1', 101, '/health/inbound')
client_MC.post_inbound_channel('inbound_channel.xml', 'inbound_channel_2', 102, '/health/inbound')
client_MC.post_inbound_channel('inbound_channel.xml', 'inbound_channel_3', 103, '/health/inbound')
client_MC.post_inbound_channel('inbound_channel.xml', 'inbound_channel_4', 104, '/health/inbound')
client_MC.post_inbound_channel('inbound_channel.xml', 'inbound_channel_5', 105, '/health/inbound')
client_MC.post_inbound_channel('inbound_channel.xml', 'inbound_channel_6', 106, '/health/inbound')
client_MC.post_inbound_channel('inbound_channel.xml', 'inbound_channel_7', 107, '/health/inbound')
client_MC.post_inbound_channel('inbound_channel.xml', 'inbound_channel_8', 108, '/health/inbound')
client_MC.post_inbound_channel('inbound_channel.xml', 'inbound_channel_9', 109, '/health/inbound')

channels = client_MC.get_channels()

print(channels)

response = client_MC.deploy_channels()

#channel_id = "f32dc40f-2aeb-49b7-8ebd-2100d40dff53"
#response = client_MC.delete_channel(channel_id)
