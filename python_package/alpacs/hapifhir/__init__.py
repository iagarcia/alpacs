import urllib3
import json

class HapiFhirClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        return
    
    def start_connection(self):
        http = urllib3.PoolManager()
        self.connection = http
        return
    
    def get_patients(self):
        headers = {
            'accept': 'application/fhir+json'}
        response = self.connection.request(
            'GET',
            'http://{}:{}/fhir/Patient'.format(self.ip, self.port),
            headers=headers)
        json_data = json.loads(response.data.decode('utf-8')) 
        return json_data
    
    def delete_patient(self, id):
        headers = {
            'accept': 'application/fhir+json'}
        response = self.connection.request(
            'DELETE',
            'http://{}:{}/fhir/Patient/{}'.format(self.ip, self.port, id),
            headers=headers)
        json_data = json.loads(response.data.decode('utf-8')) 
        return json_data
    
    def post_patient(self, patient):
        headers = {
            'Content-Type': 'application/fhir+json',
            'accept': 'application/fhir+json'}
        encoded_data = json.dumps(patient).encode('utf-8')
        response = self.connection.request(
            'POST',
            'http://{}:{}/fhir/Patient'.format(self.ip, self.port),
            headers=headers,
            body=encoded_data)
        json_data = json.loads(response.data.decode('utf-8')) 
        return json_data
    
    def get_imagingStudy(self):
        headers = {
            'accept': 'application/fhir+json'}
        response = self.connection.request(
            'GET',
            'http://{}:{}/fhir/ImagingStudy'.format(self.ip, self.port),
            headers=headers)
        json_data = json.loads(response.data.decode('utf-8')) 
        return json_data
    
    def post_imagingStudy(self, imagingStudy):
        headers = {
            'Content-Type': 'application/fhir+json',
            'accept': 'application/fhir+json'}
        encoded_data = json.dumps(imagingStudy).encode('utf-8')
        response = self.connection.request(
            'POST',
            'http://{}:{}/fhir/ImagingStudy'.format(self.ip, self.port),
            headers=headers,
            body=encoded_data)
        json_data = json.loads(response.data.decode('utf-8')) 
        return json_data
    
    def get_diagnosticReport(self):
        headers = {
            'accept': 'application/fhir+json'}
        response = self.connection.request(
            'GET',
            'http://{}:{}/fhir/DiagnosticReport'.format(self.ip, self.port),
            headers=headers)
        json_data = json.loads(response.data.decode('utf-8')) 
        return json_data
    
    def post_diagnosticReport(self, diagnosticReport):
        headers = {
            'Content-Type': 'application/fhir+json',
            'accept': 'application/fhir+json'}
        encoded_data = json.dumps(diagnosticReport).encode('utf-8')
        response = self.connection.request(
            'POST',
            'http://{}:{}/fhir/DiagnosticReport'.format(self.ip, self.port),
            headers=headers,
            body=encoded_data)
        json_data = json.loads(response.data.decode('utf-8')) 
        return json_data
