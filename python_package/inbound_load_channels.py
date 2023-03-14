import  alpacs.mirthconnect as mc

client_MC = mc.MirthConnectClient(
    "52.54.19.165",
    "8443",
    "alpacs",
    "4lp4cs!",
    "keystore.jks",
    "mirthpass"
    )
client_MC.start_connection()

start = 101
end = 109

port_range = range(start, end+1)
for i in range(len(port_range)):
    client_MC.post_inbound_channel(
        'inbound_channel.xml',
        'inbound_channel_{}'.format(i+1),
        port_range[i],
        '/health/inbound')

client_MC.deploy_channels()

channels = client_MC.get_channels()
print(channels)