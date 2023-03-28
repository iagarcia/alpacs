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

channels = 9
ip = "18.232.238.142"
port = 200
for i in range(channels):
    client_MC.post_curated_channel(
        'curated_channel.xml',
        'curated_channel_{}'.format(i+1),
        '/health/curated/channel_{}'.format(i+1),
        ip,
        port)

client_MC.deploy_channels()

channels = client_MC.get_channels()
print(channels)