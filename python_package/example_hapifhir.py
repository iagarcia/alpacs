import alpacs.hapifhir as hf
from pprint import pprint
from pydicom import dcmread
import json

client_HF = hf.HapiFhirClient(
    "52.206.137.7",
    "8090"
)
client_HF.start_connection()

pprint(client_HF.get_patients())

#pprint(client_HF.delete_patient(1))

ds = dcmread("./sample.dcm")
PatientName = ds["PatientName"]
PatientID = ds["PatientID"]

new_patient = json.load(open('patient.json'))
new_patient['name'][0]['text'] = str(PatientName.value)
new_patient['identifier'][0]['value'] = str(PatientID.value)

pprint(new_patient)
pprint(type(new_patient))

pprint(client_HF.post_patient(new_patient))

pprint(client_HF.get_patients())