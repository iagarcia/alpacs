import alpacs.hapifhir as hf
from pprint import pprint
from pydicom import dcmread
import json

client_HF = hf.HapiFhirClient(
    "52.206.137.7",
    "8090"
)
client_HF.start_connection()

#pprint(client_HF.get_patients())

#pprint(client_HF.delete_patient(1))

ds = dcmread("./dicom_samples/sample.dcm")

if ("PatientID" in ds.dir()):
    PatientID = ds["PatientID"].value
else:
    PatientID = "noID"

if ("PatientName" in ds.dir()):
    PatientName = ds["PatientName"].value
else:
    PatientName = "noName"

if ("PatientTelephoneNumbers" in ds.dir()):
    PatientTelephoneNumbers = ds["PatientTelephoneNumbers"].value
else:
    PatientTelephoneNumbers = "noPhone"

if ("PatientSex" in ds.dir()):
    PatientSex = ds["PatientSex"].value
else:
    PatientSex = "unknown"

if ("PatientBirthDate" in ds.dir()):
    PatientBirthDate = ds["PatientBirthDate"].value
else:
    PatientBirthDate = "0000-00-00"

if ("PatientAddress" in ds.dir()):
    PatientAddress = ds["PatientAddress"].value
else:
    PatientAddress = "noAddress"


new_patient = json.load(open('./fhir_resources/patient.json'))
new_patient['identifier'][0]['value'] = str(PatientID)
new_patient['name'][0]['text'] = str(PatientName)
new_patient['telecom'][0]['value'] = str(PatientTelephoneNumbers)
new_patient['gender'] = str(PatientSex)
new_patient['birthDate'] = str(PatientBirthDate)
new_patient['address'][0]['value'] = str(PatientAddress)

pprint(new_patient)
pprint(type(new_patient))

pprint(client_HF.post_patient(new_patient))

pprint(client_HF.get_patients())