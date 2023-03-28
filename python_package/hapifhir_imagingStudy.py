import alpacs.hapifhir as hf
from pprint import pprint
from pydicom import dcmread
import json

client_HF = hf.HapiFhirClient(
    "hapifhir.alpacs.cl",
    "8090"
)
client_HF.start_connection()

#pprint(client_HF.get_imagingStudy())

ds = dcmread("./dicom_samples/sample.dcm")

if ("StudyID" in ds.dir()):
    StudyID = ds["StudyID"].value
else:
    StudyID = "noStudyID"

if ("ModalitiesInStudy" in ds.dir()):
    ModalitiesInStudy = ds["ModalitiesInStudy"].value
else:
    ModalitiesInStudy = "noModalitiesInStudy"

if ("PatientID" in ds.dir()):
    PatientID = ds["PatientID"].value
else:
    PatientID = "PatientID"

if ("StudyID" in ds.dir()):
    StudyID = ds["StudyID"].value
else:
    StudyID = "noID"

if ("StudyDate" in ds.dir()):
    StudyDate = ds["StudyDate"].value
else:
    StudyDate = "0000-00-00"

if ("NumberOfStudyRelatedSeries" in ds.dir()):
    NumberOfStudyRelatedSeries = ds["NumberOfStudyRelatedSeries"].value
else:
    NumberOfStudyRelatedSeries = 0

if ("NumberOfStudyRelatedInstances" in ds.dir()):
    NumberOfStudyRelatedInstances = ds["NumberOfStudyRelatedInstances"].value
else:
    NumberOfStudyRelatedInstances = 0

if ("StudyDescription" in ds.dir()):
    StudyDescription = ds["StudyDescription"].value
else:
    StudyDescription = "noStudyDescription"

if ("SeriesInstanceUID" in ds.dir()):
    SeriesInstanceUID = ds["SeriesInstanceUID"].value
else:
    SeriesInstanceUID = "noSeriesInstanceUID"

if ("SeriesNumber" in ds.dir()):
    SeriesNumber = ds["SeriesNumber"].value
else:
    SeriesNumber = "noSeriesNumber"

if ("Modality" in ds.dir()):
    Modality = ds["Modality"].value
else:
    Modality = "noModality"

if ("SeriesDescription" in ds.dir()):
    SeriesDescription = ds["SeriesDescription"].value
else:
    SeriesDescription = "noSeriesDescription"

if ("BodyPartExamined" in ds.dir()):
    BodyPartExamined = ds["BodyPartExamined"].value
else:
    BodyPartExamined = "noBodyPartExamined"

if ("SeriesDate" in ds.dir()):
    SeriesDate = ds["SeriesDate"].value
else:
    SeriesDate = "2000-01"

if ("SOPInstanceUID" in ds.dir()):
    SOPInstanceUID = ds["SOPInstanceUID"].value
else:
    SOPInstanceUID = "noSOPInstanceUID"

if ("SOPInstanceUID" in ds.dir()):
    SOPInstanceUID = ds["SOPInstanceUID"].value
else:
    SOPInstanceUID = "noSOPInstanceUID"

if ("SOPInstanceUID" in ds.dir()):
    SOPInstanceUID = ds["SOPInstanceUID"].value
else:
    SOPInstanceUID = "noSOPInstanceUID"

if ("SOPClassUID" in ds.dir()):
    SOPClassUID = ds["SOPClassUID"].value
else:
    SOPClassUID = "SOPClassUID"

if ("InstanceNumber" in ds.dir()):
    InstanceNumber = ds["InstanceNumber"].value
else:
    InstanceNumber = "InstanceNumber"

if ("DocumentTitle" in ds.dir()):
    DocumentTitle = ds["DocumentTitle"].value
else:
    DocumentTitle = "DocumentTitle"


new_imagingStudy = json.load(open('./fhir_resources/imagingStudy.json'))
new_imagingStudy['identifier'][0]['value'] = str(StudyID)
new_imagingStudy['modality'][0]['value'] = str(ModalitiesInStudy)
new_imagingStudy['subject']['identifier']['value'] = str(PatientID)
new_imagingStudy['started'] = str(StudyDate)
new_imagingStudy['numberOfSeries'] = str(NumberOfStudyRelatedSeries)
new_imagingStudy['numberOfInstances'] = str(NumberOfStudyRelatedInstances)
new_imagingStudy['description'] = str(StudyDescription)
new_imagingStudy['series'][0]['uid'] = str(SeriesInstanceUID)
new_imagingStudy['series'][0]['number'] = str(SeriesNumber)
new_imagingStudy['series'][0]['modality'] = str(Modality)
new_imagingStudy['series'][0]['descrtiption'] = str(SeriesDescription)
new_imagingStudy['series'][0]['bodySite'] = str(BodyPartExamined)
new_imagingStudy['series'][0]['started'] = str(SeriesDate)
new_imagingStudy['series'][0]['instance'][0]['uid'] = str(SOPInstanceUID)
new_imagingStudy['series'][0]['instance'][0]['sopClass']['display'] = str(SOPClassUID)
new_imagingStudy['series'][0]['instance'][0]['number'] = str(InstanceNumber)
new_imagingStudy['series'][0]['instance'][0]['title'] = str(DocumentTitle)

pprint(new_imagingStudy)
pprint(type(new_imagingStudy))

pprint(client_HF.post_imagingStudy(new_imagingStudy))

pprint(client_HF.get_imagingStudy())