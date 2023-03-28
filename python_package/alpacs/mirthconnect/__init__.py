import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import base64
import textwrap
import jks
import xmltodict
import json
from pprint import pprint
import uuid

def write_pem(der_bytes, type, file):
    file.write("-----BEGIN %s-----\n" % type)
    text = "\r\n".join(textwrap.wrap(base64.b64encode(der_bytes).decode('ascii'), 64))
    file.write(text)
    file.write("\n-----END %s-----\n" % type)
    return

def generate_pem(keystore, keypass, user):
    ks = jks.KeyStore.load(keystore, keypass)
    file = open("{}_cert.pem".format(user), "w")
    for alias, pk in ks.private_keys.items():
        file.write("Private key: %s\n" % pk.alias)
        if pk.algorithm_oid == jks.util.RSA_ENCRYPTION_OID:
            write_pem(pk.pkey, "RSA PRIVATE KEY", file)
        else:
            write_pem(pk.pkey_pkcs8, "PRIVATE KEY", file)
        for c in pk.cert_chain:
            write_pem(c[1], "CERTIFICATE", file)
        file.write("\n")
    for alias, c in ks.certs.items():
        file.write("Certificate: %s" % c.alias)
        write_pem(c.cert, "CERTIFICATE", file)
        file.write("\n")
    for alias, sk in ks.secret_keys.items():
        file.write("Secret key: %s\n" % sk.alias)
        file.write("  Algorithm: %s\n" % sk.algorithm)
        file.write("  Key size: %d bits\n" % sk.key_size)
        file.write("  Key: %s\n" % "".join("{:02x}".format(b) for b in bytearray(sk.key)))
    file.close()
    return "{}_cert.pem".format(user)

class MirthConnectClient:
    def __init__(self, ip, port, user, password, keystore, keypass):
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.keystore = keystore
        self.keypass = keypass
        return

    def start_connection(self):
        cert = generate_pem(self.keystore, self.keypass, self.user)
        self.cert = cert
        auth_string = '{}:{}'.format(self.user, self.password)
        auth_encoded = base64.b64encode(auth_string.encode('ascii')).decode('utf-8')
        self.auth = auth_encoded
        http = urllib3.PoolManager(
            cert_file=self.cert,
            cert_reqs='CERT_NONE')
        self.connection = http
        return

    def get_users(self):
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Authorization': 'Basic {}'.format(self.auth)}
        response = self.connection.request(
            'GET',
            'https://{}:{}/api/users'.format(self.ip, self.port),
            headers=headers)
        data_dict = xmltodict.parse(response.data)
        json_data = json.dumps(data_dict['list']['user'], indent=2)
        return json_data

    def get_channels(self):
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Authorization': 'Basic {}'.format(self.auth)}
        response = self.connection.request(
            'GET',
            'https://{}:{}/api/channels'.format(self.ip, self.port),
            headers=headers)
        data_dict = xmltodict.parse(response.data)
        channels = []
        if (data_dict['list'] != None):
            channels_raw = data_dict['list']['channel']
            if (type(channels_raw) == dict):
                channels.append({
                    'id': channels_raw['id'],
                    'name': channels_raw['name'],
                    'description': channels_raw['description'],
                    'sourceConnector': channels_raw['sourceConnector'],
                    'destinationConnectors': channels_raw['destinationConnectors']
                })
            elif (type(channels_raw) == list):
                for channel in channels_raw:
                    channels.append({
                        'id': channel['id'],
                        'name': channel['name'],
                        'description': channel['description'],
                        'sourceConnector': channel['sourceConnector'],
                        'destinationConnectors': channel['destinationConnectors']
                    })
        json_data = json.dumps(channels, indent=2)
        return json_data

    def post_inbound_channel(self, channel_xml, name, port, path):
        headers = {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'Authorization': 'Basic {}'.format(self.auth)}
        
        channel = open(channel_xml, "rb")
        data_dict = xmltodict.parse(channel)
        data_dict['channel']['id'] = str(uuid.uuid4())
        data_dict['channel']['name'] = name
        data_dict['channel']['description'] = "Inbound Channel - DICOM Listener/File Writer"
        data_dict['channel']['sourceConnector']['properties']['listenerConnectorProperties']['port'] = port
        data_dict['channel']['destinationConnectors']['connector']['properties']['host'] = path

        encoded_data = json.dumps(data_dict).encode('utf-8')
        response = self.connection.request(
            'POST',
            'https://{}:{}/api/channels'.format(self.ip, self.port),
            headers=headers,
            body=encoded_data)
        return response
    
    def post_curated_channel(self, channel_xml, name, path, ip, port):
        headers = {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'Authorization': 'Basic {}'.format(self.auth)}
        
        channel = open(channel_xml, "rb")
        data_dict = xmltodict.parse(channel)
        data_dict['channel']['id'] = str(uuid.uuid4())
        data_dict['channel']['name'] = name
        data_dict['channel']['description'] = "Curated Channel - File Reader/DICOM Sender"
        data_dict['channel']['sourceConnector']['properties']['host'] = path
        data_dict['channel']['destinationConnectors']['connector']['properties']['host'] = ip
        data_dict['channel']['destinationConnectors']['connector']['properties']['port'] = port

        encoded_data = json.dumps(data_dict).encode('utf-8')
        response = self.connection.request(
            'POST',
            'https://{}:{}/api/channels'.format(self.ip, self.port),
            headers=headers,
            body=encoded_data)
        return response

    def delete_channel(self, channel_id):
        print("DELETE:", channel_id)
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Authorization': 'Basic {}'.format(self.auth)}
        response = self.connection.request(
            'DELETE',
            'https://{}:{}/api/channels?channelId={}'.format(self.ip, self.port, channel_id),
            headers=headers)
        return response
    
    def deploy_channels(self):
        print("DEPLOY CHANNELS")
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Authorization': 'Basic {}'.format(self.auth)}
        response = self.connection.request(
            'POST',
            'https://{}:{}/api/channels/_redeployAll'.format(self.ip, self.port),
            headers=headers)
        return response