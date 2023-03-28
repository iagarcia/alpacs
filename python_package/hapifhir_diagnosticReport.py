import alpacs.hapifhir as hf
from pprint import pprint
from pydicom import dcmread
import json

client_HF = hf.HapiFhirClient(
    "hapifhir.alpacs.cl",
    "8090"
)
client_HF.start_connection()

ds = dcmread("./dicom_samples/sample.dcm")

if ("StudyID" in ds.dir()):
    StudyID = ds["StudyID"].value
else:
    StudyID = "noStudyID"

new_diagnosticReport = json.load(open('./fhir_resources/diagnosticReport.json'))
new_diagnosticReport['imagingStudy'][0]['identifier']['value'] = str(StudyID)

pprint(new_diagnosticReport)
pprint(type(new_diagnosticReport))

pprint(client_HF.post_diagnosticReport(new_diagnosticReport))

pprint(client_HF.get_diagnosticReport())