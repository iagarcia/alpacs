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

client_MC.post_inbound_channel('inbound_channel.xml', 'middleware_1', 101, '/health/inbound')
client_MC.post_inbound_channel('inbound_channel.xml', 'middleware_2', 102, '/health/inbound')
client_MC.post_inbound_channel('inbound_channel.xml', 'middleware_3', 103, '/health/inbound')
client_MC.post_inbound_channel('inbound_channel.xml', 'middleware_4', 104, '/health/inbound')
client_MC.post_inbound_channel('inbound_channel.xml', 'middleware_5', 105, '/health/inbound')
client_MC.post_inbound_channel('inbound_channel.xml', 'middleware_6', 106, '/health/inbound')
client_MC.post_inbound_channel('inbound_channel.xml', 'middleware_7', 107, '/health/inbound')
client_MC.post_inbound_channel('inbound_channel.xml', 'middleware_8', 108, '/health/inbound')
client_MC.post_inbound_channel('inbound_channel.xml', 'middleware_9', 109, '/health/inbound')

channels = client_MC.get_channels()

print(channels)

response = client_MC.deploy_channels()
